import json
import os
from datetime import datetime

import pandas as pd
import requests
from bs4 import BeautifulSoup

from app.utils.config import config

os.environ["no_proxy"] = "*"
# see https://bugs.python.org/issue28342
# and https://stackoverflow.com/questions/73582293/airflow-external-api-call-gives-negsignal-sigsegv-error


def import_data():
    url = config["URL"]
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    item = soup.find_all("script")
    item = str(item[0])
    item = item.split("var")
    item = item[8].split("\n")[0].split(";")[0].strip().split("confData = ")
    file = open(config["JSON_FILE"], "w")
    file.write(item[1])
    file.close()


def transform_data(year: int):
    data_json = json.load(open(config["JSON_FILE"]))
    output_info_times_prayers = get_info_day_times_by_calendar_type(
        data_json, year, "iqamaCalendar"
    )
    output_iqama_times_prayers = get_info_day_times_by_calendar_type(
        data_json, year, "calendar"
    )
    df = pd.merge(
        save_to_df(output_info_times_prayers),
        save_to_df(output_iqama_times_prayers),
        on=["day", "name_prayers"],
    )
    df["time_jumua_1"] = data_json["jumua"]
    df["time_jumua_2"] = data_json["jumua2"]

    return df


def get_info_day_times_by_calendar_type(data, year: int, calendar_type: str):
    infos_times = []
    for month, month_values in enumerate(data[calendar_type], 1):
        for day, times in month_values.items():
            try:
                date = datetime(int(year), int(month), int(day))
                if calendar_type == "iqamaCalendar":
                    info_type = "iqama_difference"
                    tmp = [int(iqama.replace("+", "")) for iqama in times]
                    fields = tmp[
                        :
                    ]  # we don't have iqama time for shuruq prayers, by default it's 0
                    fields.insert(1, 0)
                else:
                    fields = times
                    info_type = "times_prayer"

            except ValueError:
                print("We ignore 29 febuary if it's not a bisextile year!")

            finally:
                infos_times.append(
                    {
                        "day": date,
                        "name_prayers": [
                            "Fajr",
                            "Shuruq",
                            "Dhouhr",
                            "Asr",
                            "Maghrib",
                            "Isha",
                        ],
                        info_type: fields,
                    }
                )
    return infos_times


def save_to_df(items):
    df = pd.DataFrame(items).set_index(["day"]).apply(pd.Series.explode).reset_index()
    return df


def save_df_to_csv(df):
    df.to_csv(config["CSV_FILE"], index=False)


def main(year: int):
    import_data()
    df = transform_data(year)
    save_df_to_csv(df)
