import datetime
import os

from airflow import DAG
from airflow.operators.python import PythonOperator
from app.salat_times_ingestion import main
from app.salat_times_to_db import load_data_to_db

default_args = {
    "owner": "Bsh",
    "depends_on_past": False,
    "start_date": datetime.date(2023, 1, 1),
    "retries": 1,
    "retry_delay": datetime.timedelta(minutes=1),
}

with DAG(
    dag_id="main_salat_times_pipeline",
    start_date=datetime.datetime(2023, 1, 1),
    schedule_interval=None,
    catchup=False,
    params={
        "year": 2023,
    },
) as dag:
    ingest = PythonOperator(
        task_id="main_salat_times", python_callable=main, op_args=("{{params.year}}",)
    )
    load = PythonOperator(
        task_id="export_data_to_db",
        python_callable=load_data_to_db,
        op_args=[
            f'postgresql://{os.environ.get("DB_USER")}:{os.environ.get("DB_PASSWORD")}@{os.environ.get("DB_HOST")}:'
            f'{os.environ.get("DB_PORT")}/{os.environ.get("DB_NAME")}'
        ],
    )

    ingest >> load
