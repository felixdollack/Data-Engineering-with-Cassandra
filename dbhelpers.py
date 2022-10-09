import cassandra
from cassandra.cluster import Cluster


def connect(host=["127.0.0.1"]):
    session = None
    try:
        cluster = Cluster(host)
        session = cluster.connect()
    except cassandra.cluster.NoHostAvailable as e:
        print(f"Error: could not create a Cassandra session at {host}")
        print(e)
    return cluster, session


def createKeyspace(session, keyspace, replication={'class': 'SimpleStrategy', 'replication_factor' : 1}):
    execute(session, f"CREATE KEYSPACE IF NOT EXISTS {keyspace} WITH replication = {replication};")


def setKeyspace(session, keyspace):
    execute(session, f"USE {keyspace};")


def execute(session, command, *args):
    try:
        return session.execute(command, *args)
    except cassandra.InvalidRequest as e:
        print(f"Error: could not execute command={command}")
        print(e)


def createTable(session, tablename, schema):
    execute(session, f"CREATE TABLE IF NOT EXISTS {tablename} ({schema});")


def dropTable(session, tablename):
    execute(session, f"DROP TABLE IF EXISTS {tablename};")


def insert(session, tablename, schema, values):
    value_string = f"{' '.join(['%s']*len(values)).strip().replace(' ',', ')}"
    execute(session, f"INSERT INTO {tablename} ({schema}) VALUES ({value_string})", values)


def select(session, tablename, column='*', where=''):
    addWhere = where != ''
    return execute(session, f"SELECT {column} FROM {tablename}{addWhere*' WHERE '}{where};")


def closeSession(session):
    session.shutdown()


def closeConnection(cluster, session=None):
    if session:
        closeSession(session)
    cluster.shutdown()


