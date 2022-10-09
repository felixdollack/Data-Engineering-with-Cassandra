import cql_queries
import csv
import dbhelpers


if __name__ == '__main__':
    file = 'event_datafile_new.csv'
    keyspace = 'sparkify'

    conn, sess = dbhelpers.connect()
    dbhelpers.setKeyspace(sess, keyspace)

    with open(file, encoding = 'utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader) # skip header

        for line in csvreader:
            # insert data to song_info_by_session
            values = (
                int(line[8]), int(line[3]),
                line[0], line[9], float(line[5])
            )
            dbhelpers.insert(sess, *cql_queries.song_info_by_session_insert, values)

            # insert data to song_info_by_user
            values = (
                int(line[10]), int(line[8]),
                int(line[3]), line[1], line[4],
                line[0], line[9]
            )
            dbhelpers.insert(sess, *cql_queries.song_info_by_user_insert, values)

            # insert data to user_info_by_song
            values = (
                line[9], int(line[10]), line[1], line[4]
            )
            dbhelpers.insert(sess, *cql_queries.user_info_by_song_insert, values)

    dbhelpers.closeConnection(conn, sess)
