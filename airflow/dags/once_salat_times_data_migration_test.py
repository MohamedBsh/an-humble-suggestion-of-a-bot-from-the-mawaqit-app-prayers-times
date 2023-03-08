import datetime
import os

from airflow import DAG
from airflow.operators.python import PythonOperator
from app.tests.salat_times_data_test import main

default_args = {
    "owner": "Bsh",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": datetime.timedelta(minutes=1),
}
with DAG(
        "salat_times_migration_test",
        default_args=default_args,
        description="Salat Times Migration",
        schedule_interval="@once",
        start_date=datetime.datetime(2023, 1, 1),
) as dag:
    test_data = PythonOperator(
        task_id="salat_times_data_migration_test",
        python_callable=main,
        op_args=[
            f'postgresql://{os.environ.get("DB_USER")}:{os.environ.get("DB_PASSWORD")}@{os.environ.get("DB_HOST")}:'
            f'{os.environ.get("DB_PORT")}/{os.environ.get("DB_NAME")}'
        ],
    )

    test_data
