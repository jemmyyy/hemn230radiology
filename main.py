from flask import Flask , render_template, redirect, request
from flask.templating import render_template
import mysql.connector
# from passlib.hash import sha256_crypt

mydb = mysql.connector.connect(
    host = 'localhost',
    username = 'root',
    passwd = '@Hm$d_2001',
    database = 'radiology'
    )
mycursor = mydb.cursor()
app=Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['username']
        mycursor.execute('SELECT * from credentials')
        orig = mycursor.fetchone()
        if (username == orig[0]) and (password == orig[1]):
            return render_template('home.html')
        else:
            return render_template('signin.html')
    else:
        return render_template('signin.html')

@app.route('/home')
def home():
    return render_template('/home.html')

@app.route('/doctor')
def doctor():
    return render_template('doctor.html')     

@app.route('/nurse')
def nurse():
    return render_template('nurse.html')     

@app.route('/signin')
def signin():
    return render_template('signin.html')     

@app.route('/patient')
def patient():
    return render_template('patient.html')     


@app.route('/machine')
def machine():
    return render_template('machines.html')     


@app.route('/technician')
def technician():
    return render_template('technician.html')     

@app.route('/room')
def rooms():
    return render_template('rooms.html')     

if __name__=='__main__':
    app.run(debug=True)


