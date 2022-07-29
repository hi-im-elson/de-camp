#!/usr/bin/env python
# coding: utf-8

import os
import pandas as pd
from sqlalchemy import create_engine
from time import time
import argparse


def main(params):
    
    userName = params.userName
    password = params.password
    host = params.host
    port = params.port
    databaseName = params.databaseName
    tableName = params.tableName
    url = params.url
    csvName = "covid-cases.csv"

    # download csv
    os.system(f"wget {url} -O {csvName}")

    engine = create_engine(f"postgresql://{userName}:{password}@{host}:{port}/{databaseName}")
    engine.connect()

    cols = list(pd.read_csv(csvName, nrows=1))
    dfIter = pd.read_csv(csvName, iterator=True, chunksize=10000, engine="python")
    dfPart = next(dfIter)


    dfPart.head(n=0).to_sql(con=engine, name=tableName, if_exists="replace")
    dfPart.to_sql(con=engine, name=tableName, if_exists="append", index=False)

    while True:
        timeStart = time()
        dfPart = next(dfIter)
        dfPart.to_sql(con=engine, name=tableName, if_exists="append", index=False)
        timeEnd = time()
        print("Inserted another chunk. Took %.3f second" % (timeEnd - timeStart))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--userName', help='username for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--databaseName', help='database name for postgres')
    parser.add_argument('--tableName', help='table to write results')
    parser.add_argument('--url', help='url of csv')

    args = parser.parse_args()

    main(args)


