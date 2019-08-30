import sqlite3
import pandas as pd
import os

def execute(sql):
    conn = sqlite3.connect('output.db')
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print('--------------------------------------------')
        print('[ERROR] 数据库在执行' + sql + '时发生错误.')
        print(e)
        print('--------------------------------------------')
    conn.close()

def get():
    sql_db = sqlite3.connect('output.db')
    df = pd.read_sql_query("select * from score", sql_db)
    df = df.set_index('score')
    df = df.sort_index(ascending=False)
    return df.to_html()