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
def load_from_google_cloud_storage(*args, **kwargs):
    """
    Template code for loading data from any source.

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your data loading logic here
    config_path = path.join(get_repo_path(), "io_config.yaml")
    config_profile = "default"

    bucket_name = "my-ads-data-source"
    print(args)

    object_key = args[0]["key"]

    data = GoogleCloudStorage.with_config(ConfigFileLoader(config_path, config_profile)).load(
        bucket_name,
        object_key,
    )

    data = data.astype({})

    return data
