import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Fetch variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Connect to the database
connection = psycopg2.connect(DATABASE_URL)

if connection.status == psycopg2.extensions.STATUS_READY:
    print("Database connection is active")
else:
    print("Connection status:", connection.status)

connection.close()	
