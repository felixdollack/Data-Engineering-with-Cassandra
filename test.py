import dbhelpers
import cql_queries
from prettytable import PrettyTable


if __name__ == '__main__':
    conn, sess = dbhelpers.connect()
    dbhelpers.setKeyspace(sess, 'sparkify')

    x = PrettyTable()
    x.field_names = cql_queries.select_song_info_by_session[1].split(', ')

    y = PrettyTable()
    y.field_names = cql_queries.select_song_info_by_user[1].split(', ')

    z = PrettyTable()
    z.field_names = cql_queries.select_user_info_by_song[1].split(', ')

    res = dbhelpers.select(sess, *cql_queries.select_song_info_by_session)
    for row in res:
        x.add_row(row)
    print(x)

    res = dbhelpers.select(sess, *cql_queries.select_song_info_by_user)
    for row in res:
        y.add_row(row)
    print(y)

    res = dbhelpers.select(sess, *cql_queries.select_user_info_by_song)
    for row in res:
        z.add_row(row)
    print(z)

    dbhelpers.closeConnection(conn, sess)
