variable "bucket_name_source" {
  type        = string
  description = "The name of the bucket"
}

variable "bucket_location" {
  type        = string
  default     = "europe-west1"
  description = "Location"
}

variable "project_id" {
  type        = string
  description = "GCP Project id"
}

variable "storage_class" {
  type        = string
  description = "Storage class for objects in the bucket"
}

variable "folder_path" {
  type        = string
  description = "Path to folder in which data is stored"
}

variable "zone" {
  type = string
}

variable "region" {
  type        = string
  description = "Region to deploy infra"
}

variable "publickeypath" {
  type        = string
  description = "path for rsa public key for remote connection "
}
