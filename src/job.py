import json
import requests
from bs4 import BeautifulSoup
import argparse
from transform import get_info_times_by_day
import pandas as pd
from glom import glom


class ScrapPrayersTimesPage:
    """
    pipenv run python3 src/job.py -u="https://mawaqit.net/fr/grande-mosquee-de-paris" -d="./data/output/prayers.json"
    """

    def __init__(self, url: str, data: json, year: str):
        self.url = url
        self.data = data
        self.page = requests.get(url)
        self.soup = BeautifulSoup(self.page.text, "html.parser")
        self.year = year

    def _write_to_json(self) -> str:
        item = self.soup.find_all("script")
        item = str(item[0])
        item = item.split("var")
        item = item[8].split("\n")[0].split(";")[0].strip().split("confData = ")
        file = open("data/output/prayers.json", "w")
        file.write(item[1])
        file.close()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", type=str, default=None)
    parser.add_argument("-d", "--data", type=str, default=None)

    results = parser.parse_args()
    url = results.url
    data = results.data
    YEAR = "2022"
    INFO_WANTED = "calendar"

    prayers = ScrapPrayersTimesPage(url, data, YEAR)

    # EXTRACT
    prayers._write_to_json()

    data = json.load(open(data))

    # TRANSFORM
    output = get_info_times_by_day(data, INFO_WANTED, YEAR)

    #df = pd.DataFrame.from_dict(output[0], orient='index', columns=['Fajr', 'Shuruq', 'Dhur', 'Asr', 'Magreb','Isha'])
    #print(df)

