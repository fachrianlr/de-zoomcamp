import configparser
import time

import pandas as pd
from sqlalchemy import create_engine

config = configparser.ConfigParser()
config.read('config.ini')

db_host = config.get('Database', 'host')
db_port = config.getint('Database', 'port')
db_user = config.get('Database', 'user')
db_password = config.get('Database', 'password')
db_name = config.get('Database', 'db')
table_name = config.get('Database', 'table')
csv_file = config.get('File', 'csv_file')


def ingest_data():
    print("Start Ingesting Data...")
    db_connection = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
    print(f'Connecting to database: {db_connection}')
    conn = create_engine(db_connection)

    header = pd.read_csv(csv_file, nrows=0).columns
    df_header = pd.DataFrame(columns=header)
    df_header.tpep_pickup_datetime = pd.to_datetime(df_header.tpep_pickup_datetime)
    df_header.tpep_dropoff_datetime = pd.to_datetime(df_header.tpep_dropoff_datetime)
    df_header.to_sql(table_name, conn, index=True, if_exists='replace')
    print(f"create new table : {table_name}")
    schema_table = pd.io.sql.get_schema(df_header, table_name, con=conn)
    print(schema_table)

    chunk_size = 100000
    csv_iter = pd.read_csv(csv_file, chunksize=chunk_size, iterator=True)

    total_data = 0
    start_time = time.process_time()
    print(f"start inserting data")

    for chunk in csv_iter:
        start_time_chunk = time.process_time()
        total_data += len(chunk)
        chunk.tpep_pickup_datetime = pd.to_datetime(chunk.tpep_pickup_datetime)
        chunk.tpep_dropoff_datetime = pd.to_datetime(chunk.tpep_dropoff_datetime)
        chunk.to_sql(name=table_name, con=conn, if_exists='append')
        end_time_chunk = time.process_time()
        elapsed_time_chunk = end_time_chunk - start_time_chunk
        print(f"Chunk Data Inserted: {len(chunk)}, process time: {elapsed_time_chunk:.3f} s, Total Data Inserted: {total_data}")

    end_time = time.process_time()
    elasped_time = end_time - start_time
    print(f"Total Process Time: {elasped_time:.3f} s")


if __name__ == '__main__':
    ingest_data()
