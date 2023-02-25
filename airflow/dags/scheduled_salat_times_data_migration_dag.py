import datetime
import os

from airflow import DAG
from airflow.operators.python import PythonOperator
from app.salat_times_data_migration import main

default_args = {
    "owner": "Bsh",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": datetime.timedelta(minutes=1),
}
with DAG(
    "salat_times_migration",
    default_args=default_args,
    description="Salat Times Migration",
    schedule_interval="@once",
    start_date=datetime.datetime(2022, 1, 1),
) as dag:
    create_table = PythonOperator(
        task_id="salat_times_data_migration",
        python_callable=main,
        op_args=[
            f'postgresql://{os.environ.get("DB_USER")}:{os.environ.get("DB_PASSWORD")}@{os.environ.get("DB_HOST")}:'
            f'{os.environ.get("DB_PORT")}/{os.environ.get("DB_NAME")}'
        ],
    )

    create_table
