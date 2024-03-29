import os
from datetime import datetime, timedelta

import psycopg2
import telebot
import tabulate
import pytz

from airflow import DAG
from airflow.models import Variable
from airflow.operators.python_operator import PythonOperator
from app.utils.config import config
import requests
from bs4 import BeautifulSoup

os.environ["no_proxy"] = "*"

# Initialize Telegram bot with token
bot = telebot.TeleBot(Variable.get("TELEGRAM_BOT_TOKEN"))

# Define database connection parameters
db_config = {
    "host": os.environ.get("DB_HOST"),
    "port": os.environ.get("DB_PORT"),
    "database": os.environ.get("DB_NAME"),
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASSWORD"),
}

# Define SQL query to fetch data for the current date
SQL = "SELECT * FROM salattimes WHERE day = %s;"


# Function to fetch data from Postgres and send it as a message to Telegram
def send_data_to_telegram():
    # Connect to database
    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()

    # Get the current date and time with the local timezone
    tz = pytz.timezone('Europe/Paris')
    now = datetime.now(tz)

    # Get current date in YYYY-MM-DD format
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Determine if it's winter time
    winter_start_date = datetime(now.year, 11, 1, tzinfo=tz)
    winter_end_date = datetime(now.year + 1, 3, 31, tzinfo=tz)
    is_winter_time = winter_start_date <= now < winter_end_date

    # Execute SQL query to fetch data for the current date
    cur.execute(SQL, (current_date,))

    # Get fetched data
    data = cur.fetchall()

    # Close database connection
    cur.close()
    conn.close()

    headers = [desc[0] for desc in cur.description]
    exclude_columns = [0, 4, 5]
    headers = [h for i, h in enumerate(headers) if i not in exclude_columns]
    data_without_columns = [[row[i] for i in range(len(row)) if i not in exclude_columns] for row in data]

    # display the first occurence of jumua time (session 1 and session 2).
    JUMUA_SESSION_1_INDEX = 4
    JUMUA_SESSION_2_INDEX = 5
    JUMUA_SESSION_1_VALUE = ""
    JUMUA_SESSION_2_VALUE = ""
    for row in data:
        if JUMUA_SESSION_1_VALUE == "" and row[JUMUA_SESSION_1_INDEX]:
            JUMUA_SESSION_1_VALUE = row[JUMUA_SESSION_1_INDEX]
        if JUMUA_SESSION_2_VALUE == "" and row[JUMUA_SESSION_2_INDEX]:
            JUMUA_SESSION_2_VALUE = row[JUMUA_SESSION_2_INDEX]
        if JUMUA_SESSION_1_VALUE != "" and JUMUA_SESSION_2_VALUE != "":
            break

    # Use tabulate to format the data as a table
    table = tabulate.tabulate(data_without_columns, headers=headers)

    # Prepare message text
    message_text = "Horaires de prières pour {}:\n\n".format(current_date)
    message_text += "```\n{}\n```".format(table)

    # Decrease Jumuaa time by one hour if it's Friday and in winter time
    if now.weekday() == 4 and is_winter_time:
        JUMUA_SESSION_1_VALUE -= datetime.timedelta(hours=1)
        JUMUA_SESSION_2_VALUE -= datetime.timedelta(hours=1)

    # Check if it's Friday to display the "Jumuaa - Créneau" information
    if now.weekday() == 4:
        message_text += "\n\nJumuaa - Créneau 1: {}".format(JUMUA_SESSION_1_VALUE)
        message_text += "\nJumuaa - Créneau 2: {}".format(JUMUA_SESSION_2_VALUE)

    # Send message to Telegram bot
    bot.send_message(chat_id=Variable.get("TELEGRAM_CHAT_ID"), text=message_text, parse_mode="markdown")

    # Make a request to another web page to extract duaas text
    DUAAS_PATH = config["DUAAS_URL"]
    response = requests.get(DUAAS_PATH)

    if response.status_code == 404:
        print("Error 404: Duaas not found")
    else:
        html_content = response.content

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    message_text_duaas = "```\n\n\n```"
    message_text_duaas += "Le rappel profite au croyant. Voici quelques duaas importantes:"

    for h2_tag in soup.find_all('h2'):
        message_text_duaas += f'\n\n{h2_tag.text}\n'
        for p_tag in h2_tag.find_next_sibling('div').find_all('p'):
            message_text_duaas += f'{p_tag.text}\n'

    bot.send_message(chat_id=Variable.get("TELEGRAM_CHAT_ID"), text=message_text_duaas, parse_mode="markdown")


# Define DAG parameters
default_args = {
    "owner": "Bsh",
    "depends_on_past": False,
    "start_date": datetime.now().replace(hour=0, minute=0, second=0, microsecond=0),
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

# Define DAG object
with DAG(
        "send_data_to_telegram",
        default_args=default_args,
        description="Fetch data from Postgres and send it to MawaqitPrayersTimeParisBot",
        schedule_interval="0 0 * * *",
) as dag:
    # Define DAG tasks
    send_data = PythonOperator(
        task_id="send_data", python_callable=send_data_to_telegram, dag=dag
    )

    send_data
