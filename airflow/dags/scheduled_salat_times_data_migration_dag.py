import datetime
from airflow import DAG
from airflow.models import Variable
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'Bsh',
    'depends_on_past': False,
    'retries': 1,
    "retry_delay": datetime.timedelta(minutes=1),
}
with DAG(
        'salat_times_migration',
        default_args=default_args,
        description='Salat Times Migration',
        schedule_interval="@once",
        start_date=datetime.datetime(2022, 1, 1),
        catchup=False
) as dag:

    t1 = BashOperator(
        task_id='salat_times_migration',
        bash_command='pipenv run python3 app/salat_times_data_migration.py '
                     '--connection %s' % Variable.get("dev_connection")
    )
