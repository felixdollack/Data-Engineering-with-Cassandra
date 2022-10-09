# Data Modeling with Cassandra (Udacity Data Engineer Nanodegree)
This project contains an ETL pipeline for the fictionary startup Sparkify.

The purpose of the pipeline is to analyze what songs users are listening to.

The data is part of the [Million Song Dataset] and comes as CSV user logs and song metadata.

An Apache Cassandra (NoSQL) database with a star schema is setup with analytic focus and optimized queries for song plays.


## Data:
The data is a subset of the [Million Song Dataset] converted into CSV files of daily song plays.

Example of song play user data:
```
artist,auth,firstName,gender,itemInSession,lastName,length,level,location,method,page,registration,sessionId,song,status,ts,userId
,Logged In,Walter,M,0,Frye,,free,"San Francisco-Oakland-Hayward, CA",GET,Home,1.54092E+12,38,,200,1.54111E+12,39
...
```


### Files included:
- README.md (this file)
- cql_queries.py
- setup_keyspace_and_tables.py
- etl.py
- merge_data.py
- test.py

- createDockerCassandra.sh
- restartDockerCassandra.sh


### Requirements:
- a running Apache Cassandra server
- cassandra package
- data from the [Million Song Dataset] in `event_data/`


## Run:
1. Start a local Cassandra docker container.
```
# only the very first time
docker pull cassandra
./createDockerCassandra.sh
```
the subsequent times executing below script is sufficient:
```
./restartDockerCassandra.sh
```

2. Create the database schema and fill in the data.
```
# connect to the database and create the schema
python setup_keyspace_and_tables.py

# prepare the data
python merge_data.py

# read the CSV file and fill the database
python etl.py
```

3. Test your creation
```
python test.py
```

4. To shutdown the running docker container press `CTRL+C`.

[Million Song Dataset]: http://millionsongdataset.com
