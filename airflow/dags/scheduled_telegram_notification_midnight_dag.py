import os
import psycopg2
import telebot
from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import timedelta

# Initialize Telegram bot with token
bot = telebot.TeleBot(os.environ.get("TELEGRAM_TOKEN"))

# Define database connection parameters
db_config = {
    "host": os.environ.get("DB_HOST"),
    "port": os.environ.get("DB_PORT"),
    "database": os.environ.get("DB_NAME"),
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASSWORD")
}

# Define SQL query to fetch data for the current date
SQL = "SELECT * FROM salattimes WHERE day = %s;"

# Function to fetch data from Postgres and send it as a message to Telegram
def send_data_to_telegram():
    # Connect to database
    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()

    # Get current date in YYYY-MM-DD format
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Execute SQL query to fetch data for the current date
    cur.execute(SQL, (current_date,))

    # Get fetched data
    data = cur.fetchall()

    # Close database connection
    cur.close()
    conn.close()

    # Prepare message text
    message_text = "Prayers Times for {}:\n".format(current_date)
    for row in data:
        message_text += "{}\n".format(row)

    # Send message to Telegram bot
    bot.send_message(chat_id=os.environ.get("TELEGRAM_CHAT_ID"), text=message_text)

# Define DAG parameters
default_args = {
    "owner": "Bsh",
    "depends_on_past": False,
    "start_date": datetime.now().replace(hour=0, minute=0, second=0, microsecond=0),
    "retries": 1,
    "retry_delay": timedelta(minutes=1)
}

# Define DAG object
dag = DAG(
    "send_data_to_telegram",
    default_args=default_args,
    description="Fetch data from Postgres and send it to MawaqitPrayersTimeParisBot",
    schedule_interval="0 0 * * *"
)

# Define DAG tasks
send_data = PythonOperator(
    task_id="send_data",
    python_callable=send_data_to_telegram,
    dag=dag
)
