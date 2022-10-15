def pad_month(data):
    month_padded = dict((key, key.zfill(2)) for key in data["calendar"][0])
    return dict([(month_padded.get(k), v) for k, v in data["calendar"][0].items()])
