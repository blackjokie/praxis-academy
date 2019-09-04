import mysql.connector as asu
from mysql.connector import Error

try:
    konak = asu.connect(host='localhost', database='movie_rent', user='blackjokie', password='12345')
    if konak.is_connected():
        db_info = konak.get_server_info()
        print("Connected to MySQL Server version ", db_info)
        cursor = konak.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Your connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if (konak.is_connected()):
        cursor.close()
        konak.close()
        print("MySQL connection is closed")