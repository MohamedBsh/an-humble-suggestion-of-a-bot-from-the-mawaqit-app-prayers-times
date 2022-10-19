import json
import requests
from bs4 import BeautifulSoup
import argparse
from transform import get_info_times_by_day


class ScrapPrayersTimesPage:
    """
    pipenv run python3 src/job.py -u="https://mawaqit.net/fr/grande-mosquee-de-paris" -f="./data/output/prayers.json"
    """

    def __init__(self, url: str, year: str):
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
    YEAR = "2022"
    INFO_WANTED = "calendar"

    prayers = ScrapPrayersTimesPage(url, YEAR)

    # EXTRACT
    prayers._write_to_json(filename)

    data = json.load(open(filename))

    # TRANSFORM
    output = get_info_times_by_day(data, INFO_WANTED, YEAR)

    #df = pd.DataFrame.from_dict(output[0], orient='index', columns=['Fajr', 'Shuruq', 'Dhur', 'Asr', 'Magreb','Isha'])
    #print(df)

