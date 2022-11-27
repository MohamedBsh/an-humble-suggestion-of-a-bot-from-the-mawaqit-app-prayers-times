import argparse
from app.model import Connection


def migration(db_connection: str):
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


def main(connection: str):
    migration(connection)
