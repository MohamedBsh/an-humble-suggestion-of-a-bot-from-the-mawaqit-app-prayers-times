from sqlalchemy import Column, Date, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Connection(object):
    def __init__(self, db_connection):
        engine = create_engine(db_connection)
        self.engine = engine

    def get_session(self):
        Session = sessionmaker(bind=self.engine)

        return Session()

    def get_engine(self):
        return self.engine


Base = declarative_base()


def init_db(db_connection):
    engine = create_engine(db_connection)
    Base.metadata.create_all(bind=engine)


class SalatTimes(Base):
    __tablename__ = "salattimes"

    day = Column(Date, primary_key=True)
    name_prayers = Column(String, primary_key=True)
    times_prayer = Column(String)
    iqama_difference = Column(Integer)
    time_jumua_1 = Column(String)
    time_jumua_2 = Column(String)

    def __init__(
        self,
        day,
        name_prayers,
        times_prayer,
        iqama_difference,
        time_jumua_1,
        time_jumua_2,
    ):
        self.day = day
        self.name_prayers = name_prayers
        self.times_prayer = times_prayer
        self.iqama_difference = iqama_difference
        self.time_jumua_1 = time_jumua_1
        self.time_jumua_2 = time_jumua_2
