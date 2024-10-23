from sqlalchemy import create_engine
import pandas as pd
import os
import sys


user = "TBD"
password = "TBD"
server = "127.0.0.1"
port = "5432
db = "postgres"
table_prefix = "stg"

def sanitize_name(col_name: str) -> str:
    return (col_name
        .lower()
        .replace(":", "")
        .replace(" ", "_")
        .replace("-", "_")
        .replace(".", "_")
        .replace("/", "_")
        .replace("(", "")
        .replace(")", "")
        .replace("&", "and")
        )

def tablename_from_filename(filename: str) -> str:
    file = os.path.splitext(filename)[0]
    table_name = sanitize_name(file)
    return table_name

def extract(infile -> str) -> None:
    try:
        df = pd.read_csv(infile, low_memory=False)
        df.columns = [sanitize_name(c) for c in df.columns]
        table_name = tablename_from_filename(os.path.basename(infile))
        load_data(df, table_name)
    except Exception as e:
        print(f"columns: {str(df.columns)}")
        print(f"data extraction error: {str(e)}")

def load_data(df: pd.DataFrame, table_name: str) -> None:
    try:
        engine = create_engine(f"postgresql://{user}:{password}@{server}:{port}/{db}")
        print(f"importing {len(df)} records to {db}/{table}")
        df.to_sql(f"{table_prefix}_{table_name}", engine, if_exists="replace", index=False)
        print("data import successful")
    except Exception as e:
        print(f"Failed to load the data: {str(e)}")

if __name__ == "__main__":
    infile = sys.argv[1]
    load_data(infile)
