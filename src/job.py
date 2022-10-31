import json
import requests
from bs4 import BeautifulSoup
import argparse
from transform import get_info_times_prayers_by_day, get_iqama_times_prayers_by_day
import pandas as pd


class ScrapPrayersTimesPage:
    """
    pipenv run python3 src/job.py -u="https://mawaqit.net/fr/grande-mosquee-de-paris" -f="./data/output/prayers.json"
    """

    def __init__(self, url: str, year: int):
        self.url = url
        self.page = requests.get(url)
        self.soup = BeautifulSoup(self.page.text, "html.parser")
        self.year = year

    def _write_to_json(self, filename: str) -> str:
        item = self.soup.find_all("script")
        item = str(item[0])
        item = item.split("var")
        item = item[8].split("\n")[0].split(";")[0].strip().split("confData = ")
        file = open(filename, "w")
        file.write(item[1])
        file.close()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", type=str, default=None)
    parser.add_argument("-f", "--filename", type=str, default=None)

    results = parser.parse_args()
    url = results.url
    filename = results.filename
    YEAR = 2022

    prayers = ScrapPrayersTimesPage(url, YEAR)

    # EXTRACT
    prayers._write_to_json(filename)

    data = json.load(open(filename))

    # TRANSFORM
    output_info_times_prayers = get_info_times_prayers_by_day(data, YEAR)
    output_iqama_times_prayers = get_iqama_times_prayers_by_day(data, YEAR)

    df_info_times_prayers = pd.DataFrame(output_info_times_prayers).set_index(['day']).apply(pd.Series.explode).reset_index()
    df_iqama_times_prayers = pd.DataFrame(output_iqama_times_prayers).set_index(['day']).apply(pd.Series.explode).reset_index()
    df_salat_times_enriched = pd.merge(df_info_times_prayers, df_iqama_times_prayers, on=["day", "name_prayers"])
    df_salat_times_enriched["time_jumua_1"] = data["jumua"]
    df_salat_times_enriched["time_jumua_2"] = data["jumua2"]

    df_salat_times_enriched.to_csv("./data/output/salat_times.csv", index=False)

