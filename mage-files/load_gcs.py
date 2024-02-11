from os import path
from typing import Dict, List

from google.cloud import storage
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from mage_ai.settings.repo import get_repo_path

if "data_loader" not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if "test" not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_from_google_cloud_storage(*args, **kwargs) -> List[List[Dict]]:
    """
    Template for loading data from a Google Cloud Storage bucket.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#googlecloudstorage
    """
    config_path = path.join(get_repo_path(), "io_config.yaml")
    config_profile = "default"

    object_keys = []
    metadata = []

    bucket_name = "my-ads-data-source"
    object_key = "my-ads-data-source/data/"

    google_cloud_storage_loader = GoogleCloudStorage.with_config(ConfigFileLoader(config_path, config_profile))

    objects = google_cloud_storage_loader.client.list_blobs(bucket_name)

    # Iterators for blob objects can only be used once so we need to store them into another list type variable
    objects = list(objects)

    object_keys = [{"key": i.name} for i in objects]
    metadata = [{"block_uuid": "for_" + i.name} for i in objects]

    out = [object_keys, metadata]

    print(out)
    return out
