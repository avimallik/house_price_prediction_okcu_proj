from flask import Flask, request, jsonify, render_template
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'hpp_db'
mysql = MySQL(app)

print(mysql)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register', methods = ['POST', 'GET'])
def register():
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
    
    return render_template('register.html', msg=msg)


if __name__ == "__main__":
       app.debug = True
       app.run()
