from datetime import datetime


def get_info_times_prayers_by_day(data, year: int):
    return [{'day': datetime(year, month+1, int(day)), 'name_prayers': ['Fajr', 'Shuruq', 'Dhouhr', 'Asr', 'Maghrib', 'Isha'], 'times': time} for month, month_values in enumerate(data["calendar"]) for day, time in month_values.items()]