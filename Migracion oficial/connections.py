import pyodbc
import mysql.connector 
from mysql.connector import Error 

def connect_sqlserver() -> pyodbc.Connection:
    return pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=DESKTOP-H1RNTOQ;"
        "Database=GimnasioPremier;" 
        "Trusted_Connection=yes;"
    )

def connect_mysqll() -> mysql.connector.connection.MySQLConnection:
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Moonraker3*", 
    )
