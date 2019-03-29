from flask import Flask, session, redirect, url_for, escape, request, render_template 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)
app.secret_key=b'supersecret1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/db.db'
db = SQLAlchemy(app)
@app.route('/',methods=['GET','POST'])
@app.route('/login',methods=['GET','POST'])
def login():

    if 'name' in session:
        return redirect(url_for('home')) 

    elif request.method=='POST':
        results = db.engine.execute(text("select * from users"))
        for result in results: 
            if result['email'] == request.form['email']:
                if result['password'] == request.form['password']:
                    fillSession(result)
                    return redirect(url_for('home')) 
                else: # if pass isnt correct, go back
                    return render_template('index.html')

        return render_template('index.html')

    elif request.method=='GET':
        return render_template('index.html')

def fillSession(result):
    if 'email' not in session:
        session['email'] = result['email']
        session['typ'] = result['type']
        session['name'] = result['name']


def query(requested_data):
    # returns bundle of requested data
    # could request: 
    # instructor: feedback, all student grades
    # students : students grades
    data = []# package of data depending on requested
    if session['typ'] == 'INSTRUCTOR':
        if requested_data == "FEEDBACK":
            sql = """
            select name,reviews from users 
            left join feedback on users.email == feedback.email
            where users.email == {}""".format(session['email'])
            data = db.engine.execute(text(sql))
        elif requested_data == "ALLGRADES":#requesting all student grades
            data = db.engine.execute(text('select * from grades'))

    else:# else, its a student requesting his grades
        if requested_data == "MYGRADES":
            sql = """
            select name, a1,a2,a3,q1,q2,q3,q4,midterm,final from users 
            left join grades 
            on users.studentNumber == grades.studentNumber
            where type != "INSTRUCTOR" and users.email =={}
            """.format(session['email'])
            data = db.engine.execute(text(sql))
    return data

    


######similar pages####### V
@app.route('/CWork')
def a():
    return render_template('CWork.html', data= session['name'])

@app.route('/instructor')
def b():
    return render_template('instructor.html', data= session['name'])

@app.route('/Ohour')
def c():
    return render_template('Ohour.html', data= session['name'])

#####instructor pages##### V
@app.route('/myFeedBack')#need query info
def d():
    lstF = []
    data = query("FEEDBACK")
    for i in data:
        fbs = i['reviews']
        # review will look like 'this is a review $# this is another $#'
        start = 0
        for end in range(1,len(fbs)):
            if fbs[end] == '#' and fbs[end - 1] == '$':
                lstF.append(fbs[start:end - 1])
                start = end + 1
        return render_template('myFeedBack.html', data=lstF, name = session['name'])

@app.route('/gradesAll')#need query info
def f():
    return render_template('gradesAll.html', data=query("ALLGRADES"), name = session['name'])

#####student pages##### V
@app.route('/Feedback') 
def g():
    return render_template('Feedback.html', data= session['name'])

@app.route('/gradesMy')#need query info
def i():
    data = query("MYGRADES")
    for i in data:
        return render_template('gradesMy.html', data=i)

##### home ####### V
@app.route('/home')
def home():
    if session['typ'] == 'INSTRUCTOR':
        return render_template('homeInstructor.html', data= session['name'])
    else:
        return render_template('homeStudent.html', data = session['name'])

######log out############
@app.route('/logout')
def logout():
    if 'name' in session:
        session.pop('name')
    
    if 'email' in session:
        session.pop('email')

    if 'typ' in session:
        session.pop('typ')
    
    return redirect(url_for('login')) 

if __name__ =="__main__":
    app.run(debug=True)