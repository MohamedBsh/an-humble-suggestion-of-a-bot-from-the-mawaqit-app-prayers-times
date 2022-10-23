import json
from src.transform import get_iqama_times_prayers_by_day, get_info_times_prayers_by_day
import datetime


def test_pad_month_3_days_january():
    data = json.load(open("tests/mock_data/calendar-sample-01-2022-3-days.json"))
    year = "2022"
    assert get_info_times_prayers_by_day(data, year) == [
        {
            "day": datetime.datetime(2022, 1, 1, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:49", "08:44", "12:55", "14:47", "17:08", "18:47"],
        },
        {
            "day": datetime.datetime(2022, 1, 2, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:49", "08:44", "12:56", "14:48", "17:09", "18:48"],
        },
        {
            "day": datetime.datetime(2022, 1, 3, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:49", "08:44", "12:56", "14:49", "17:10", "18:49"],
        },
    ]


def test_pad_one_month_january():
    data = json.load(open("tests/mock_data/calendar-sample-01-2022.json"))
    year = "2022"
    assert get_info_times_prayers_by_day(data, year) == [
        {
            "day": datetime.datetime(2022, 1, 1, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:49", "08:44", "12:55", "14:47", "17:08", "18:47"],
        },
        {
            "day": datetime.datetime(2022, 1, 2, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:49", "08:44", "12:56", "14:48", "17:09", "18:48"],
        },
        {
            "day": datetime.datetime(2022, 1, 3, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:49", "08:44", "12:56", "14:49", "17:10", "18:49"],
        },
        {
            "day": datetime.datetime(2022, 1, 4, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:49", "08:44", "12:57", "14:50", "17:11", "18:50"],
        },
        {
            "day": datetime.datetime(2022, 1, 5, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:49", "08:44", "12:57", "14:51", "17:12", "18:51"],
        },
        {
            "day": datetime.datetime(2022, 1, 6, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:49", "08:43", "12:58", "14:52", "17:13", "18:52"],
        },
        {
            "day": datetime.datetime(2022, 1, 7, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:49", "08:43", "12:58", "14:53", "17:14", "18:53"],
        },
        {
            "day": datetime.datetime(2022, 1, 8, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:49", "08:43", "12:59", "14:54", "17:15", "18:54"],
        },
        {
            "day": datetime.datetime(2022, 1, 9, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:49", "08:42", "12:59", "14:55", "17:17", "18:55"],
        },
        {
            "day": datetime.datetime(2022, 1, 10, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:48", "08:42", "12:59", "14:56", "17:18", "18:56"],
        },
        {
            "day": datetime.datetime(2022, 1, 11, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:48", "08:41", "13:00", "14:57", "17:19", "18:58"],
        },
        {
            "day": datetime.datetime(2022, 1, 12, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:48", "08:41", "13:00", "14:59", "17:21", "18:59"],
        },
        {
            "day": datetime.datetime(2022, 1, 13, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:47", "08:40", "13:01", "15:00", "17:22", "19:00"],
        },
        {
            "day": datetime.datetime(2022, 1, 14, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:47", "08:39", "13:01", "15:01", "17:23", "19:01"],
        },
        {
            "day": datetime.datetime(2022, 1, 15, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:46", "08:39", "13:01", "15:02", "17:25", "19:02"],
        },
        {
            "day": datetime.datetime(2022, 1, 16, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:46", "08:38", "13:02", "15:03", "17:26", "19:03"],
        },
        {
            "day": datetime.datetime(2022, 1, 17, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:45", "08:37", "13:02", "15:05", "17:28", "19:05"],
        },
        {
            "day": datetime.datetime(2022, 1, 18, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:45", "08:36", "13:02", "15:06", "17:29", "19:06"],
        },
        {
            "day": datetime.datetime(2022, 1, 19, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:44", "08:36", "13:03", "15:07", "17:31", "19:07"],
        },
        {
            "day": datetime.datetime(2022, 1, 20, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:44", "08:35", "13:03", "15:08", "17:32", "19:08"],
        },
        {
            "day": datetime.datetime(2022, 1, 21, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:43", "08:34", "13:03", "15:10", "17:34", "19:10"],
        },
        {
            "day": datetime.datetime(2022, 1, 22, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:42", "08:33", "13:03", "15:11", "17:35", "19:11"],
        },
        {
            "day": datetime.datetime(2022, 1, 23, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:41", "08:32", "13:04", "15:12", "17:37", "19:12"],
        },
        {
            "day": datetime.datetime(2022, 1, 24, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:41", "08:31", "13:04", "15:13", "17:38", "19:14"],
        },
        {
            "day": datetime.datetime(2022, 1, 25, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:40", "08:30", "13:04", "15:15", "17:40", "19:15"],
        },
        {
            "day": datetime.datetime(2022, 1, 26, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:39", "08:28", "13:04", "15:16", "17:41", "19:16"],
        },
        {
            "day": datetime.datetime(2022, 1, 27, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:38", "08:27", "13:05", "15:17", "17:43", "19:18"],
        },
        {
            "day": datetime.datetime(2022, 1, 28, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:37", "08:26", "13:05", "15:19", "17:45", "19:19"],
        },
        {
            "day": datetime.datetime(2022, 1, 29, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:36", "08:25", "13:05", "15:20", "17:46", "19:21"],
        },
        {
            "day": datetime.datetime(2022, 1, 30, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:35", "08:23", "13:05", "15:21", "17:48", "19:22"],
        },
        {
            "day": datetime.datetime(2022, 1, 31, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:34", "08:22", "13:05", "15:23", "17:50", "19:23"],
        },
        {
            "day": datetime.datetime(2022, 2, 1, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:33", "08:21", "13:05", "15:24", "17:51", "19:25"],
        },
        {
            "day": datetime.datetime(2022, 2, 2, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:32", "08:19", "13:06", "15:25", "17:53", "19:26"],
        },
        {
            "day": datetime.datetime(2022, 2, 3, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:30", "08:18", "13:06", "15:27", "17:54", "19:28"],
        },
        {
            "day": datetime.datetime(2022, 2, 4, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:29", "08:16", "13:06", "15:28", "17:56", "19:29"],
        },
        {
            "day": datetime.datetime(2022, 2, 5, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:28", "08:15", "13:06", "15:29", "17:58", "19:31"],
        },
        {
            "day": datetime.datetime(2022, 2, 6, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:27", "08:13", "13:06", "15:31", "17:59", "19:32"],
        },
        {
            "day": datetime.datetime(2022, 2, 7, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:25", "08:12", "13:06", "15:32", "18:01", "19:33"],
        },
        {
            "day": datetime.datetime(2022, 2, 8, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:24", "08:10", "13:06", "15:33", "18:03", "19:35"],
        },
        {
            "day": datetime.datetime(2022, 2, 9, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:23", "08:09", "13:06", "15:35", "18:04", "19:36"],
        },
        {
            "day": datetime.datetime(2022, 2, 10, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:21", "08:07", "13:06", "15:36", "18:06", "19:38"],
        },
        {
            "day": datetime.datetime(2022, 2, 11, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:20", "08:06", "13:06", "15:37", "18:08", "19:39"],
        },
        {
            "day": datetime.datetime(2022, 2, 12, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:18", "08:04", "13:06", "15:39", "18:09", "19:41"],
        },
        {
            "day": datetime.datetime(2022, 2, 13, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:17", "08:02", "13:06", "15:40", "18:11", "19:42"],
        },
        {
            "day": datetime.datetime(2022, 2, 14, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:15", "08:00", "13:06", "15:41", "18:13", "19:44"],
        },
        {
            "day": datetime.datetime(2022, 2, 15, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:14", "07:59", "13:06", "15:42", "18:14", "19:45"],
        },
        {
            "day": datetime.datetime(2022, 2, 16, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:12", "07:57", "13:06", "15:44", "18:16", "19:47"],
        },
        {
            "day": datetime.datetime(2022, 2, 17, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:11", "07:55", "13:06", "15:45", "18:18", "19:48"],
        },
        {
            "day": datetime.datetime(2022, 2, 18, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:09", "07:53", "13:06", "15:46", "18:19", "19:50"],
        },
        {
            "day": datetime.datetime(2022, 2, 19, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:08", "07:52", "13:06", "15:47", "18:21", "19:51"],
        },
        {
            "day": datetime.datetime(2022, 2, 20, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:06", "07:50", "13:06", "15:49", "18:22", "19:52"],
        },
        {
            "day": datetime.datetime(2022, 2, 21, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:05", "07:48", "13:05", "15:50", "18:24", "19:54"],
        },
        {
            "day": datetime.datetime(2022, 2, 22, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:03", "07:46", "13:05", "15:51", "18:26", "19:55"],
        },
        {
            "day": datetime.datetime(2022, 2, 23, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:02", "07:44", "13:05", "15:52", "18:27", "19:56"],
        },
        {
            "day": datetime.datetime(2022, 2, 24, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:00", "07:42", "13:05", "15:53", "18:29", "19:58"],
        },
        {
            "day": datetime.datetime(2022, 2, 25, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["05:59", "07:40", "13:05", "15:55", "18:31", "19:59"],
        },
        {
            "day": datetime.datetime(2022, 2, 26, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["05:57", "07:38", "13:05", "15:56", "18:32", "20:00"],
        },
        {
            "day": datetime.datetime(2022, 2, 27, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["05:55", "07:36", "13:05", "15:57", "18:34", "20:02"],
        },
        {
            "day": datetime.datetime(2022, 2, 28, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["05:54", "07:35", "13:04", "15:58", "18:35", "20:03"],
        },
    ]


def test_get_iqama_time_two_months():
    data = json.load(open("tests/mock_data/iqama-sample-01-02-2022.json"))
    year = "2022"
    assert get_iqama_times_prayers_by_day(data, year) == [
        {
            "day": datetime.datetime(2022, 1, 1, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 1, 2, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 1, 3, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 1, 4, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 1, 5, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 1, 6, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 1, 7, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 1, 8, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 1, 9, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 1, 10, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 1, 11, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 1, 12, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 1, 13, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 1, 14, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 1, 15, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 1, 16, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 1, 17, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 1, 18, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 1, 19, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 1, 20, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 1, 21, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 1, 22, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 1, 23, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 1, 24, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 1, 25, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 1, 26, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 1, 27, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 1, 28, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 1, 29, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 1, 30, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 1, 31, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 2, 1, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 2, 2, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 2, 3, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 2, 4, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 2, 5, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 2, 6, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 2, 7, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 2, 8, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 2, 9, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 2, 10, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 2, 11, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 2, 12, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 2, 13, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 2, 14, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 2, 15, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 2, 16, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 2, 17, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 2, 18, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 2, 19, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 2, 20, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 2, 21, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 2, 22, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 2, 23, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 2, 24, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 2, 25, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 2, 26, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 2, 27, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
        {
            "day": datetime.datetime(2022, 2, 28, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": [8, 8, 8, 0, 8],
        },
    ]


def test_get_info_times_prayers_by_day_two_months():
    data = json.load(open("tests/mock_data/calendar-sample-01-02-2022.json"))
    year = "2022"
    assert get_info_times_prayers_by_day(data, year) == [
        {
            "day": datetime.datetime(2022, 1, 1, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:49", "08:44", "12:55", "14:47", "17:08", "18:47"],
        },
        {
            "day": datetime.datetime(2022, 1, 2, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:49", "08:44", "12:56", "14:48", "17:09", "18:48"],
        },
        {
            "day": datetime.datetime(2022, 1, 3, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:49", "08:44", "12:56", "14:49", "17:10", "18:49"],
        },
        {
            "day": datetime.datetime(2022, 1, 4, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:49", "08:44", "12:57", "14:50", "17:11", "18:50"],
        },
        {
            "day": datetime.datetime(2022, 1, 5, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:49", "08:44", "12:57", "14:51", "17:12", "18:51"],
        },
        {
            "day": datetime.datetime(2022, 1, 6, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:49", "08:43", "12:58", "14:52", "17:13", "18:52"],
        },
        {
            "day": datetime.datetime(2022, 1, 7, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:49", "08:43", "12:58", "14:53", "17:14", "18:53"],
        },
        {
            "day": datetime.datetime(2022, 1, 8, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:49", "08:43", "12:59", "14:54", "17:15", "18:54"],
        },
        {
            "day": datetime.datetime(2022, 1, 9, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:49", "08:42", "12:59", "14:55", "17:17", "18:55"],
        },
        {
            "day": datetime.datetime(2022, 1, 10, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:48", "08:42", "12:59", "14:56", "17:18", "18:56"],
        },
        {
            "day": datetime.datetime(2022, 1, 11, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:48", "08:41", "13:00", "14:57", "17:19", "18:58"],
        },
        {
            "day": datetime.datetime(2022, 1, 12, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:48", "08:41", "13:00", "14:59", "17:21", "18:59"],
        },
        {
            "day": datetime.datetime(2022, 1, 13, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:47", "08:40", "13:01", "15:00", "17:22", "19:00"],
        },
        {
            "day": datetime.datetime(2022, 1, 14, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:47", "08:39", "13:01", "15:01", "17:23", "19:01"],
        },
        {
            "day": datetime.datetime(2022, 1, 15, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:46", "08:39", "13:01", "15:02", "17:25", "19:02"],
        },
        {
            "day": datetime.datetime(2022, 1, 16, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:46", "08:38", "13:02", "15:03", "17:26", "19:03"],
        },
        {
            "day": datetime.datetime(2022, 1, 17, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:45", "08:37", "13:02", "15:05", "17:28", "19:05"],
        },
        {
            "day": datetime.datetime(2022, 1, 18, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:45", "08:36", "13:02", "15:06", "17:29", "19:06"],
        },
        {
            "day": datetime.datetime(2022, 1, 19, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:44", "08:36", "13:03", "15:07", "17:31", "19:07"],
        },
        {
            "day": datetime.datetime(2022, 1, 20, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:44", "08:35", "13:03", "15:08", "17:32", "19:08"],
        },
        {
            "day": datetime.datetime(2022, 1, 21, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:43", "08:34", "13:03", "15:10", "17:34", "19:10"],
        },
        {
            "day": datetime.datetime(2022, 1, 22, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:42", "08:33", "13:03", "15:11", "17:35", "19:11"],
        },
        {
            "day": datetime.datetime(2022, 1, 23, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:41", "08:32", "13:04", "15:12", "17:37", "19:12"],
        },
        {
            "day": datetime.datetime(2022, 1, 24, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:41", "08:31", "13:04", "15:13", "17:38", "19:14"],
        },
        {
            "day": datetime.datetime(2022, 1, 25, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:40", "08:30", "13:04", "15:15", "17:40", "19:15"],
        },
        {
            "day": datetime.datetime(2022, 1, 26, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:39", "08:28", "13:04", "15:16", "17:41", "19:16"],
        },
        {
            "day": datetime.datetime(2022, 1, 27, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:38", "08:27", "13:05", "15:17", "17:43", "19:18"],
        },
        {
            "day": datetime.datetime(2022, 1, 28, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:37", "08:26", "13:05", "15:19", "17:45", "19:19"],
        },
        {
            "day": datetime.datetime(2022, 1, 29, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:36", "08:25", "13:05", "15:20", "17:46", "19:21"],
        },
        {
            "day": datetime.datetime(2022, 1, 30, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:35", "08:23", "13:05", "15:21", "17:48", "19:22"],
        },
        {
            "day": datetime.datetime(2022, 1, 31, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:34", "08:22", "13:05", "15:23", "17:50", "19:23"],
        },
        {
            "day": datetime.datetime(2022, 2, 1, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:33", "08:21", "13:05", "15:24", "17:51", "19:25"],
        },
        {
            "day": datetime.datetime(2022, 2, 2, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:32", "08:19", "13:06", "15:25", "17:53", "19:26"],
        },
        {
            "day": datetime.datetime(2022, 2, 3, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:30", "08:18", "13:06", "15:27", "17:54", "19:28"],
        },
        {
            "day": datetime.datetime(2022, 2, 4, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:29", "08:16", "13:06", "15:28", "17:56", "19:29"],
        },
        {
            "day": datetime.datetime(2022, 2, 5, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:28", "08:15", "13:06", "15:29", "17:58", "19:31"],
        },
        {
            "day": datetime.datetime(2022, 2, 6, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:27", "08:13", "13:06", "15:31", "17:59", "19:32"],
        },
        {
            "day": datetime.datetime(2022, 2, 7, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:25", "08:12", "13:06", "15:32", "18:01", "19:33"],
        },
        {
            "day": datetime.datetime(2022, 2, 8, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:24", "08:10", "13:06", "15:33", "18:03", "19:35"],
        },
        {
            "day": datetime.datetime(2022, 2, 9, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:23", "08:09", "13:06", "15:35", "18:04", "19:36"],
        },
        {
            "day": datetime.datetime(2022, 2, 10, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:21", "08:07", "13:06", "15:36", "18:06", "19:38"],
        },
        {
            "day": datetime.datetime(2022, 2, 11, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:20", "08:06", "13:06", "15:37", "18:08", "19:39"],
        },
        {
            "day": datetime.datetime(2022, 2, 12, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:18", "08:04", "13:06", "15:39", "18:09", "19:41"],
        },
        {
            "day": datetime.datetime(2022, 2, 13, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:17", "08:02", "13:06", "15:40", "18:11", "19:42"],
        },
        {
            "day": datetime.datetime(2022, 2, 14, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:15", "08:00", "13:06", "15:41", "18:13", "19:44"],
        },
        {
            "day": datetime.datetime(2022, 2, 15, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:14", "07:59", "13:06", "15:42", "18:14", "19:45"],
        },
        {
            "day": datetime.datetime(2022, 2, 16, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:12", "07:57", "13:06", "15:44", "18:16", "19:47"],
        },
        {
            "day": datetime.datetime(2022, 2, 17, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:11", "07:55", "13:06", "15:45", "18:18", "19:48"],
        },
        {
            "day": datetime.datetime(2022, 2, 18, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:09", "07:53", "13:06", "15:46", "18:19", "19:50"],
        },
        {
            "day": datetime.datetime(2022, 2, 19, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:08", "07:52", "13:06", "15:47", "18:21", "19:51"],
        },
        {
            "day": datetime.datetime(2022, 2, 20, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:06", "07:50", "13:06", "15:49", "18:22", "19:52"],
        },
        {
            "day": datetime.datetime(2022, 2, 21, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:05", "07:48", "13:05", "15:50", "18:24", "19:54"],
        },
        {
            "day": datetime.datetime(2022, 2, 22, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:03", "07:46", "13:05", "15:51", "18:26", "19:55"],
        },
        {
            "day": datetime.datetime(2022, 2, 23, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:02", "07:44", "13:05", "15:52", "18:27", "19:56"],
        },
        {
            "day": datetime.datetime(2022, 2, 24, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["06:00", "07:42", "13:05", "15:53", "18:29", "19:58"],
        },
        {
            "day": datetime.datetime(2022, 2, 25, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["05:59", "07:40", "13:05", "15:55", "18:31", "19:59"],
        },
        {
            "day": datetime.datetime(2022, 2, 26, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["05:57", "07:38", "13:05", "15:56", "18:32", "20:00"],
        },
        {
            "day": datetime.datetime(2022, 2, 27, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["05:55", "07:36", "13:05", "15:57", "18:34", "20:02"],
        },
        {
            "day": datetime.datetime(2022, 2, 28, 0, 0),
            "name_prayers": ["Fajr", "Shuruq", "Dhouhr", "Asr", "Maghrib", "Isha"],
            "times": ["05:54", "07:35", "13:04", "15:58", "18:35", "20:03"],
        },
    ]
