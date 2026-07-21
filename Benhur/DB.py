import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("databaseURL")

connection = psycopg2.connect(DATABASE_URL)

if connection.status == psycopg2.extensions.STATUS_READY:
    print("Database connection is active")
else:
    print("Connection status:", connection.status)

connection.close()