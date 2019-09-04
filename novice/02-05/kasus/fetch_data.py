#!/usr/bin/env python3

import pymysql

# Open database connection
db = pymysql.connect("<hostname>","<username>","<password>","<db_name>")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT member.f_name, movie.n_movie from member INNER JOIN movie ON member.id_member = movie.id_member WHERE member.f_name = 'Janet Jones'"
      
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   print(results)
except:
   print ("Error: unable to fetch data")

# disconnect from server
db.close()