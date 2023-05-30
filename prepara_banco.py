# import mysql.connector
# from mysql.connector import errorcode
import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

connection = pymysql.connect(
    host=os.getenv('MYSQL_HOST'),
    user=os.getenv('MYSQL_USER'),
    password=os.getenv('MYSQL_PASSWORD'),
    database=os.getenv('MYSQL_DATABASE'),
)

with connection:
    with connection.cursor() as cursor:
        # SQL
        print(cursor)