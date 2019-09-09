import pymysql
from app import app
from db_config import mysql
from flask import jsonify, flash, request
from werkzeug import generate_password_hash, check_password_hash

@app.route('/movies')
def movie():
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sql = "SELECT * FROM movie"
            cursor.execute(sql)
            rows = cursor.fetchall()
            resp = jsonify(rows)
            resp.status_code = 200
            return resp
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    app.run()