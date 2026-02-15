from airflow import DAG
from airflow.providers.google.cloud.operators.dataflow import (
    DataflowTemplatedJobStartOperator
)
from datetime import datetime

PROJECT_ID = "ranjanrishi-project"
REGION = "us-central1"
TEMPLATE_PATH = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

default_args = {
    "start_date": datetime(2024, 1, 1),
}

with DAG(
    "trigger_dataflow_classic_template",
    schedule_interval=None,
    default_args=default_args,
    catchup=False,
) as dag:

    start_dataflow = DataflowTemplatedJobStartOperator(
        task_id="start_dataflow_job",
        template=TEMPLATE_PATH,
        project_id=PROJECT_ID,
        location=REGION,
        dataflow_default_options={},
        parameters={
            "javascriptTextTransformGcsPath": "gs://rameshsamplebucket/accounts_udf_trans.js",
            "javascriptTextTransformFunctionName": "transform",
            "JSONPath": "gs://rameshsamplebucket/accounts_bq_schema.json",
            "inputFilePattern": "gs://rameshsamplebucket/Datafile_accounts.csv",
            "outputTable": "ranjanrishi-project:testdataset.account",
            "bigQueryLoadingTemporaryDirectory": "gs://ramtempbucket7"
        },
    )

    start_dataflow