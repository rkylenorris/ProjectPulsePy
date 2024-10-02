import pandas as pd
import sqlite3


def convert_tasks_to_df(tasks: list) -> pd.DataFrame:
    return pd.DataFrame([task.__dict__ for task in tasks])


def load_df_to_sqlite(df, db_path, table_name):
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists='append', index=False)
