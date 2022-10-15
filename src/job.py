import json
import requests
from bs4 import BeautifulSoup
import argparse
from transform import get_info_times_by_day


class ScrapPrayersTimesPage:
    """
    pipenv run python3 src/job.py --url="https://mawaqit.net/fr/grande-mosquee-de-paris" --data="./data/output/prayers.json"
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
    parser.add_argument(
        "--url",
        action="store",
        dest="url",
        default=None,
        help="url link",
        required=True,
    )
    parser.add_argument(
        "--data",
        action="store",
        default=None,
        help="json data path",
        required=True,
    )
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