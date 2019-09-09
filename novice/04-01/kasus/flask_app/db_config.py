from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = '<user>'
app.config['MYSQL_DATABASE_PASSWORD'] = '<pass>'
app.config['MYSQL_DATABASE_DB'] = '<db_name>'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)