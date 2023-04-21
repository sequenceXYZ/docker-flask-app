from mysql.connector import connect, Error
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(BASE_DIR, '.env')

with open(env_path) as f:
    for line in f:
        key, value = line.strip().split('=')
        os.environ[key] = value

username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')
database = os.environ.get('DATABASE')
host = os.environ.get('HOST')


def create_connection():
    try:
        connection = connect(
            host=mysql,  # container name in docker compose file
            user=username,
            password=password,
            database=database
        )
        print("Connection established")
        return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
