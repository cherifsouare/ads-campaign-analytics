## Requirements

No requirements.

## Providers

| Name | Version | | ---------------------------------------------------------- | ------- | |
<a name="provider_google"></a> [google](#provider_google) | 5.9.0 | | <a name="provider_null"></a>
[null](#provider_null) | 3.2.2 |

## Modules

No modules.

## Resources

| Name | Type | |
\---------------------------------------------------------------------------------------------------------------------------------------------------
| -------- | |
[google_bigquery_dataset.dataset](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigquery_dataset)
| resource | |
[google_compute_instance.default](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance)
| resource | |
[google_compute_network.custom](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_network)
| resource | |
[google_compute_subnetwork.custom](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_subnetwork)
| resource | |
[google_storage_bucket.source](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket)
| resource | |
[google_storage_bucket_iam_member.member](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket_iam_member)
| resource | |
[null_resource.upload_folder_content](https://registry.terraform.io/providers/hashicorp/null/latest/docs/resources/resource)
| resource |

## Inputs

| Name | Description | Type | Default | Required | |
-------------------------------------------------------------------------------------------- |
--------------------------------------------- | -------- | ---------------- | :------: | |
<a name="input_bucket_location"></a> [bucket_location](#input_bucket_location) | Location | `string` | `"europe-west1"`
| no | | <a name="input_bucket_name_source"></a> [bucket_name_source](#input_bucket_name_source) | The name of the
bucket | `string` | n/a | yes | | <a name="input_folder_path"></a> [folder_path](#input_folder_path) | Path to folder in
which data is stored | `string` | n/a | yes | | <a name="input_project_id"></a> [project_id](#input_project_id) | GCP
Project id | `string` | n/a | yes | | <a name="input_publickeypath"></a> [publickeypath](#input_publickeypath) | path
for rsa public key for remote connection | `string` | n/a | yes | | <a name="input_region"></a> [region](#input_region)
| Region to deploy infra | `string` | n/a | yes | | <a name="input_storage_class"></a>
[storage_class](#input_storage_class) | Storage class for objects in the bucket | `string` | n/a | yes | |
<a name="input_zone"></a> [zone](#input_zone) | n/a | `string` | n/a | yes |

## Outputs

No outputs.

<!-- END_TF_DOCS -->
