from flask import Response
import os
import socket
import json
from flask import request
import mysql.connector

conn = None

class DBManager:

    def __init__(self, database = "example"):

        credentials = json.loads(os.getenv('credentials'))
        username = credentials["username"]
        password = credentials["password"]
        host = credentials["host"]

        # username = os.getenv('username')
        # password = os.getenv('password')
        # host = os.getenv('host')


        self.connection = mysql.connector.connect(
            user=username, 
            password=password,
            host=host, 
            database=database,
            auth_plugin='mysql_native_password'
        )
        self.cursor = self.connection.cursor()
    
    def populate_db(self):
        #timestamp = timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        #self.cursor.execute('INSERT INTO transactions (col) VALUES (%s)', (timestamp))
        self.cursor.execute('INSERT INTO transactions (col) VALUES (CURRENT_TIMESTAMP())')
        self.connection.commit()

# Create a handler for our read (POST) app
def add_date_timestamp():
    """
    This function responds to a request for /app
    This actually adds timestamp to database

    """
    # Create the list of people from our data
    global conn
    if not conn:
        conn = DBManager()
        conn.populate_db()
    else:
        conn.populate_db()

    #return Response(status=200, mimetype='application/json')
    return Response(status=200, mimetype='application/json')
