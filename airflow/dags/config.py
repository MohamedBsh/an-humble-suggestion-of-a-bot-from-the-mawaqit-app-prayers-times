import os

SALAT_TIMES_API = os.getenv("SALAT_TIMES_API", "https://mawaqit.net/fr/grande-mosquee-de-paris")
CSV_FILE_DIR = os.getenv("CSV_FILE_DIR", "airflow/dags/datasets/output_salat_times/output.csv")
JSON_FILE_DIR = os.getenv("JSON_FILE_DIR", "airflow/dags/datasets/ingest_salat_times/output.json")

PSQL_DB = os.getenv("PGSQL_DB", "XXX")
PSQL_USER = os.getenv("PGSQL_USER", "XXX")
PSQL_PASSWORD = os.getenv("PGSQL_PASSWORD", "XXX")
PSQL_PORT = os.getenv("PGSQL_PORT", "XXX")
PSQL_HOST = os.getenv("PGSQL_HOST", "XXX")