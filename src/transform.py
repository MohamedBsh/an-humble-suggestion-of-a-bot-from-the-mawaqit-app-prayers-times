from datetime import datetime


def get_info_times_prayers_by_day(data, year: int):
    prayers_info = []
    for month, month_values in enumerate(data["calendar"], 1):
        for day, time in month_values.items():
            try:
                prayers_info.append({'day': datetime(year, month, int(day)), 'name_prayers': ['Fajr', 'Shuruq', 'Dhouhr', 'Asr', 'Maghrib', 'Isha'], 'times_prayer': time})
            except: # ignore 29 febuary if it's not a bisextile year
                pass
    return prayers_info


def get_iqama_times_prayers_by_day(data, year: int):
    iqama_info = []
    for month, month_values in enumerate(data["iqamaCalendar"], 1):
        for day, iqamas in month_values.items():
            try:
                iqamas_times = [int(iqama.replace('+', '')) for iqama in iqamas]
                add_shuruq_iqama = iqamas_times[:] # we don't have iqama time for shuruq prayers, by default it's 0
                add_shuruq_iqama.insert(1, 0)
                iqama_info.append({'day': datetime(year, month, int(day)), 'name_prayers': ['Fajr', 'Shuruq', 'Dhouhr', 'Asr', 'Maghrib', 'Isha'], 'iqama_difference': add_shuruq_iqama})
            except: # ignore 29 febuary if it's not a bisextile year
                pass
    return iqama_info