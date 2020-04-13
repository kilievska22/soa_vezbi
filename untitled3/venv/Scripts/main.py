import sqlalchemy as db
engine = db.create_engine(
    "postgresql+pg8000://postgres:yourPassword@localhost/social",
    isolation_level="READ UNCOMMITTED"
)
connection = engine.connect()
metadata = db.MetaData()
users = db.Table('users', metadata, autoload=True, autoload_with=engine)

query=db.select([users])
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
print(ResultSet)
query = db.insert(users).values( username='naveen', password='60000.00')
ResultProxy = connection.execute(query)
query=db.select([users])
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
print(ResultSet)