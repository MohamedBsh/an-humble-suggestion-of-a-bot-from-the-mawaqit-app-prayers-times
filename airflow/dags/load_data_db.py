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
            row_salat_times = SalatTimes(day=row['day'],
                                name_prayers=row['name_prayers'],
                                times_prayer=row['times_prayer'],
                                iqama_difference=row['iqama_difference'],
                                time_jumua_1=row['time_jumua_1'],
                                time_jumua_2 =row['time_jumua_2'])
            data_insert.append(row_salat_times)

    connection = Connection(db_connection)
    session = connection.get_session()
    session.add_all(data_insert)
    session.commit()
    session.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--connection", required=True, type=str)
    args = parser.parse_args()
    main(args.connection)