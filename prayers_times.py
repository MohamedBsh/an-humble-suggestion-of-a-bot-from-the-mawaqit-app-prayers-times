import requests
from bs4 import BeautifulSoup
import json


class PrayersTimesPage:
    def __init__(self, url: str):
        self.url = url
        self.page = requests.get(url)
        self.soup = BeautifulSoup(self.page.text, 'html.parser')

    def _get_times_prayers_of_the_day(self) -> str:
        item = self.soup.find_all('script')
        item = str(item[0])
        item = item.split('var')
        item = item[8].split('\n')[0].split(';')[0].strip().split('confData = ')
        item = json.loads(item[1])
        return item["times"]

    def _get_calendar_times(self) -> str:
        item = self.soup.find_all('script')
        item = str(item[0])
        item = item.split('var')
        item = item[8].split('\n')[0].split(';')[0].strip().split('confData = ')
        item = json.loads(item[1])
        return item["calendar"] # annual historic times prayers from 01.01.2022

    def _get_iqama_times(self) -> str:
        item = self.soup.find_all('script')
        item = str(item[0])
        item = item.split('var')
        item = item[8].split('\n')[0].split(';')[0].strip().split('confData = ')
        item = json.loads(item[1])
        return item["iqamaCalendar"]

    def _get_jumua_time_first_session(self) -> str:
        item = self.soup.find_all('script')
        item = str(item[0])
        item = item.split('var')
        item = item[8].split('\n')[0].split(';')[0].strip().split('confData = ')
        item = json.loads(item[1])
        return item["jumua"]

    def _get_jumua_time_second_session(self) -> str:
        item = self.soup.find_all('script')
        item = str(item[0])
        item = item.split('var')
        item = item[8].split('\n')[0].split(';')[0].strip().split('confData = ')
        item = json.loads(item[1])
        return item["jumua2"]

    def _get_shuruq_times(self) -> str:
        item = self.soup.find_all('script')
        item = str(item[0])
        item = item.split('var')
        item = item[8].split('\n')[0].split(';')[0].strip().split('confData = ')
        item = json.loads(item[1])
        return item["shuruq"]
