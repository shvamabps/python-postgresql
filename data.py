import matplotlib.pyplot as plt
import pandas as pd
import psycopg2

from config import config


def plot(sql="", filename=""):
    # read the connection parameters
    params = config()
    # connect to the PostgreSQL server
    conn = psycopg2.connect(**params)
    cur = conn.cursor()

    data = pd.read_sql(sql, conn)
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    cur.close()
    conn.close()
