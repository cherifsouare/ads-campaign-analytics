![GitHub Repo stars](https://img.shields.io/github/stars/cherifsouare/ads-campaign-analytics?style=social&color=blue)
![GitHub forks](https://img.shields.io/github/forks/cherifsouare/ads-campaign-analytics?style=social&color=blue)

# ads-campaign-analytics

## Project Overview

One of the most important aspects of keeping strategy on track for digital and marketing teams using lead generation
tools like Google Ads is the ability to assess the success of their campaigns and understand how improvements can be
made. The native integration between Google Ads and BigQuery via the
[BigQuery Data Transfer Service](https://cloud.google.com/bigquery/docs/google-ads-transfer) offers a pratical way to
load and build reporting and analytics for this purpose. However, this approach has some
[limitations](https://www.optimizesmart.com/google-ads-data-to-bigquery/#Google_data_transfer_vs_Google_Ads_API)
including the lack of control and flexibility on the volume of data to transfer which can be
[overwhelming](https://medium.com/@Buczynski/make-sense-of-your-google-ads-data-in-bigquery-using-data-build-tool-58b0443f1c8b).

Another pratical way is to use the Google Ads API to get the data on all or specific campaigns.

This project presents a comprehensive data pipeline that follows an ELT approach where raw data is extracted from the
Google API, loaded and transformed in the warehouse, and then connected to a BI tool for displaying aggregated metrics.

## Architecture

The project is designed with the following technologies to support the requirements above.

- **Terraform**: For provisioning, managing our infra and uploading raw data from local directory into our storage in
  GCP.
- **Google Cloud Storage**: for storing the raw data.
- **Google Compute Engine**: for providing a virtual machine to support our extract and load operation.
- **Docker + Mage**: for orchestrating the extract from cloud storage and loading into our data warehouse.
- **BigQuery**: serves as a data warehouse for data processing
- **dbt**: use to transform and model our data.
- **Tableau**: for data vizualization and analysis.

## Testing

This is instructions on how to test this repo. All tests are located inside the `tests` folder. We are using `pytest`.
Run the following steps.

1. docker build --tag my-project .
2. `docker-compose up test`

Add your unit tests to files inside the `tests` folder ... name your files `test_somename.py`

## Data Flow

- **Data Source**: We use some mock up data in JSON format, similar to the outputs from quering the Google Ads API. High
  level description of data source(s) and sink(s), as well as the general pattern and data flow through the pipeline.
  Discuss any assumptions made.

## Hooks

If you have your own hooks, you can add them to git-hooks.

Use this command to add them to the appropriate folder then commit.

`sh git-hooks/copy_hooks.sh`

Whatever is copied from git-hooks/copy_hooks.sh will replace anything set up using the pre-commit.
