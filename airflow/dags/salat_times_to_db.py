import argparse
import csv

from model import Connection, SalatTimes
import config


def main(db_connection):
    filename = config.CSV_FILE_DIR
    data_insert = []

    with open(filename, encoding='utf-8') as csvf:
        csv_reader = csv.DictReader(csvf)
        for row in csv_reader:
            #salat_times_data = SalatTimes(day=row['day'],
            #                    name_prayers=row['name_prayers'],
            #                    times_prayer=row['times_prayer'],
            #                    iqama_difference=row['iqama_difference'],
            #                    time_jumua_1=row['time_jumua_1'],
            #                    time_jumua_2 =row['time_jumua_2'])
            data_insert.append(row)

    connection = Connection(db_connection)
    session = connection.get_session()

    query = "INSERT INTO salattimes(day, name_prayers, times_prayer, iqama_difference, time_jumua_1, time_jumua_2) VALUES(%s,%s,%s,%s,%s,%s)"
    for data in data_insert:
        session.execute(query, data["day"], data["name_prayers"], data["times_prayer"], data["iqama_difference"], data["time_jumua_1"], data["time_jumua_2"])
    session.commit()
    session.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--connection", required=True, type=str)
    args = parser.parse_args()
    main(args.connection)