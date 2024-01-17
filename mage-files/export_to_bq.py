from mage_ai.settings.repo import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_big_query(df: DataFrame,data_2, **kwargs) -> None:
    """
    Template for exporting data to a BigQuery warehouse.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#bigquery
    """
    # Set project and dataset and table name
    project = 'analytics-exports-407122'
    dataset_id = 'ads_campaign_raw'
    table_name = data_2

    print(type(df))
    print(type(data_2))


    table_id = f"{project}.{dataset_id}.{table_name}"
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    
    BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).export(
        df,
        table_id,
        if_exists='replace',  # Specify resolution policy if table name already exists
    )
