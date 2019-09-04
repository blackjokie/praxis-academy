from flask import Flask, render_template, request
import pymysql as asu

app = Flask(__name__)

@app.route('/')
def list():
        # Open database connection
        db = asu.connect("localhost","blackjokie","12345","movie_rent" )
        
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        
        # Prepare SQL query to INSERT a record into the database.
        sql = "SELECT member.f_name, movie.n_movie from member INNER JOIN movie ON member.id_member = movie.id_member WHERE member.f_name = 'Janet Jones'"
        
        # Execute the SQL command
        cursor.execute(sql)
        
        # Fetch all the rows in a list of lists.
        isi = cursor.fetchall()
        
        return render_template('template.html', rows=isi)

if __name__ == '__main__':
    app.run(debug = True)