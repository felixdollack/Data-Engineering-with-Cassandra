from cql_queries import table_queries
import dbhelpers
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Did not receive keyspace argument!\nUsage:')
        print('python create_tables_and_keyspace <keyspace_name>')
        sys.exit()
    else:
        keyspace = sys.argv[1]
    cluster, session = dbhelpers.connect()
    dbhelpers.createKeyspace(session, keyspace)
    dbhelpers.setKeyspace(session, keyspace)
    for (tablename, schema) in table_queries:
        dbhelpers.dropTable(session, tablename)
        dbhelpers.createTable(session, tablename, schema)
    dbhelpers.closeConnection(cluster, session)
