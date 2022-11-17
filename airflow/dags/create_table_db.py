import argparse
from model import Connection


def main(db_connection):
    connection = Connection(db_connection)
    session = connection.get_session()
    session.execute('''CREATE TABLE IF NOT EXISTS salattimes (
    day DATE,
    name_prayers VARCHAR,
    times_prayer VARCHAR,
    iqama_difference INT,
    time_jumua_1 VARCHAR,
    time_jumua_2 VARCHAR,
    primary key (day, name_prayers)
    );
    ''')
    session.commit()
    session.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--connection", required=True, type=str)
    args = parser.parse_args()
    main(args.connection)