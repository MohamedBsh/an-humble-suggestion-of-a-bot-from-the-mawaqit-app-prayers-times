def get_info_times_by_day(data, info_wanted: str, year: str):
    times = []
    for k in range(len(data[info_wanted])):
        tmp_key_date = dict(
            (key, year + "-" + str(k + 1).zfill(2) + "-" + key.zfill(2))
            for key in data[info_wanted][k]
        )
        info_dict = dict(
            [(tmp_key_date.get(k), v) for k, v in data[info_wanted][k].items()]
        )
        times.append(info_dict)
    return times