import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from app.extract_salat_times import main

default_args = {
    "owner": "my_organization",
    "depends_on_past": False,
    "start_date": datetime.date(2022, 1, 1),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": datetime.timedelta(minutes=1),
}

with DAG(
        dag_id="main_salat_times_pipeline",
        start_date=datetime.datetime(2022, 1, 1),
        schedule_interval=None,
        catchup=False,
        params={
            'year': 2022,
        }
) as dag:

    ingest = PythonOperator(task_id="main_salat_times", python_callable=main, op_args=("{{params.year}}",))

    ingest
