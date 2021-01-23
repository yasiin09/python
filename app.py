from flask import Flask,render_template, request
from flask_mysqldb import MySQL
#from flask_bootstrap import Bootstrap
import yaml

import os
app = Flask(__name__)
#boostsrap işlemi

db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


@app.route('/', methods=['GET','POST'] )
def index():
    if request.method == 'POST':
        form = request.form
        name = form['name']
        age = form['age']
        password = form['password']
        cur = mysql.connection.cursor()
        #cur.execute("INSERT INTO employee(name, age) VALUES(%s,%s)", (nam
        # e, age))
        cur.execute("INSERT INTO employee(name, age, password) VALUES(%s,%s,%s)", (name, age, password))
        mysql.connection.commit() 
    return render_template('index.html')  #get için


@app.route('/employees')
def enployess():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM employee")
    if result > 0 :
        data = cur.fetchall()
        return render_template('employees.html', employees = data)





