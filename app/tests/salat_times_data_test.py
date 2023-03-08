from app.model import Connection, SalatTimes

session = Connection.get_session()
num_duplicates = session.query(SalatTimes).distinct(SalatTimes.day, SalatTimes.name_prayers, SalatTimes.times_prayer,
                                                    SalatTimes.iqama_difference, SalatTimes.time_jumua_1,
                                                    SalatTimes.time_jumua_2).count()

print(f"Number of duplicate rows: {session.query(SalatTimes).count() - num_duplicates}")
session.close()
