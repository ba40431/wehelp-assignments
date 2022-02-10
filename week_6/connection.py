import mysql.connector
from dbutils.pooled_db import PooledDB

pool=PooledDB(
    creator=mysql.connector.connect,
    mincached=2,
    maxcached=5,
    maxconnections=20,
    blocking=True,
    host="localhost",
    port="3306",
    user="root",
    password="12345678",
    database="website"
)
connection=pool.connection()
cursor=connection.cursor()

cursor.close()
connection.close()