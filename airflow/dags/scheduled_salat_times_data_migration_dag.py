import datetime

from airflow import DAG
from airflow.models import Variable
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
    t1 = PythonOperator(
        task_id="salat_times_data_migration",
        python_callable=main,
        op_args=(Variable.get("dev_connection"),),
    )

    t1
