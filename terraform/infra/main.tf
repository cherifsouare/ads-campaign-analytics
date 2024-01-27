
# Create cloud storage bucket
resource "google_storage_bucket" "source" {
  name          = var.bucket_name_source
  storage_class = var.storage_class
  location      = var.bucket_location
  force_destroy = true
}

# Grant relevant role for cloud storage buck created above
resource "google_storage_bucket_iam_member" "member" {
  bucket     = google_storage_bucket.source.name
  role       = "roles/storage.admin"
  member     = "allUsers"
  depends_on = [google_storage_bucket.source]
}
# Upload ads data in storage bucket
resource "null_resource" "upload_folder_content" {
  depends_on = [google_storage_bucket.source, google_storage_bucket_iam_member.member]
  triggers = {
    file_hashes = jsonencode({
      for fn in fileset(var.folder_path, "**") :
      fn => filesha256("${var.folder_path}/${fn}")
    })
  }

  provisioner "local-exec" {
    command = "gsutil cp -r ${var.folder_path}/* gs://${var.bucket_name_source}/data"
  }
}

# Create and configure compute_instances
resource "google_compute_instance" "default" {
  name         = "my-vm"
  machine_type = "n1-standard-1"
  zone         = var.zone

  boot_disk {
    initialize_params {
      image = "ubuntu-minimal-2210-kinetic-amd64-v20230126"
    }

  }

  network_interface {
    network = "default"
    access_config {}
  }
}

# Start vpc_compute_basic_vm_custom_vpc_network
resource "google_compute_network" "custom" {
  name                    = "my-network"
  auto_create_subnetworks = false
}


#  Start vpc_compute_basic_vm_custom_vpc_subnet
resource "google_compute_subnetwork" "custom" {
  name          = "my-subnet"
  ip_cidr_range = "10.0.1.0/24"
  region        = var.region
  network       = google_compute_network.custom.id
}

# Create dataset in BigQuery
resource "google_bigquery_dataset" "dataset" {
  dataset_id    = "ads_campaign_raw"
  project       = var.project_id
  friendly_name = "ads_campaign_raw"
  description   = "Storing the ads campaign raw data loaded from Cloud storage"
  location      = "EU"
}