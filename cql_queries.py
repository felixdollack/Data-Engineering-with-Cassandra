# TABLE NAME, SCHEMA

table_queries = [
    ('song_info_by_session', 'sessionId int, itemInSession int, artist text, song text, duration float, PRIMARY KEY(sessionId, itemInSession)'),
    ('song_info_by_user', 'userId int, sessionId int, itemInSession int, firstName text, lastName text, artist text, song text, PRIMARY KEY(userId, sessionId, itemInSession)'),
    ('user_info_by_song', 'song text, userId int, firstName text, lastName text, PRIMARY KEY(song, userId)')
]


# INSERT RECORDS

song_info_by_session_insert = (
    table_queries[0][0], 'sessionId, itemInSession, artist, song, duration'
)

song_info_by_user_insert = (
    table_queries[1][0], 'userId, sessionId, itemInSession, firstName, lastName, artist, song'
)

user_info_by_song_insert = (
    table_queries[2][0], 'song, userId, firstName, lastName'
)


# FIND INFO

select_song_info_by_session = (
    table_queries[0][0], 'artist, song, duration', 'sessionId = 338 AND itemInSession = 4'
)

select_song_info_by_user = (
    table_queries[1][0], 'artist, song, firstName, lastName', 'userId = 10 AND sessionID = 182'
)

select_user_info_by_song = (
    table_queries[2][0], 'song, firstName, lastName', "song = 'All Hands Against His Own'"
)
