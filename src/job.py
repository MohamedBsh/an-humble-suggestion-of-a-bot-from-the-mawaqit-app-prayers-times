import requests
from bs4 import BeautifulSoup
import argparse


class ScrapPrayersTimesPage:
    def __init__(self, url: str):
        self.url = url
        self.page = requests.get(url)
        self.soup = BeautifulSoup(self.page.text, "html.parser")

    def _write_to_json(self) -> str:
        item = self.soup.find_all("script")
        item = str(item[0])
        item = item.split("var")
        item = item[8].split("\n")[0].split(";")[0].strip().split("confData = ")
        file = open("data/output_prayers.json", "w")
        file.write(item[1])
        file.close()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="This is the main.py script for test")
    parser.add_argument(
        "--url",
        action="store",
        dest="url",
        default=None,
        help="<Required> url link",
        required=True,
    )
    results = parser.parse_args()
    url = results.url
    prayers = ScrapPrayersTimesPage(url)
    prayers._write_to_json()
