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
    if 'email' in session:
        data = getData(session['email'])
        return query(data)

    elif request.method=='POST':
        results = db.engine.execute(text("select * from users"))
        for result in results: 
            if result['email'] == request.form['email']:
                if result['password'] == request.form['password']:
                    return query(result)
                else:
                    return render_template('index.html')

        return render_template('index.html')

    elif request.method=='GET':
        return render_template('index.html')

def query(result):
    data = {}
    if result['type'] == "INSTRUCTOR":
        sql = """
            select name,reviews from users 
            left join feedback on users.email == feedback.email
            where users.email == {}""".format(result['email'])
        session['email'] = result['email']
        session['typ'] = result['type']
        #returns instructor name and reviews
        data = db.engine.execute(text(sql))

    else:# if user is a student
        sql = """
            select name, a1,a2,a3,q1,q2,q3,q4,midterm,final from users 
            left join grades 
            on users.studentNumber == grades.studentNumber
            where type != "INSTRUCTOR" and users.email =={}
            """.format(result['email'])
        session['email'] = result['email']
        session['typ'] = result['type']
        data = db.engine.execute(text(sql))
    
    return goToHome(data)

def getData(email):
    results = db.engine.execute(text("select * from users"))
    for result in results: 
        if result['email'] == email:
            return result

######similar pages####### V
@app.route('/CWork')
def a():
    return render_template('CWork.html')

@app.route('/instructor')
def b():
    return render_template('instructor.html')

@app.route('/Ohour')
def c():
    return render_template('Ohour.html')

#####instructor pages##### V
@app.route('/myFeedBack')
def d():
    return render_template('myFeedBack.html')

@app.route('/gradesAll')
def f():
    return render_template('gradesAll.html')

#####student pages##### V
@app.route('/Feedback')
def g():
    return render_template('Feedback.html')

@app.route('/gradesMy')
def i():
    return render_template('gradesMy.html')

##### home ####### V
@app.route('/home')
def goToHome(data = None):
    if data:
        if session['typ'] == 'INSTRUCTOR':
            return render_template('homeInstructor.html',data=data)
        else:
            return render_template('homeStudent.html',data=data)
    else: 
        data = getData(session['email'])
        return query(data)

######log out############
@app.route('/logout')
def logout():
    session.pop('email')
    session.pop('typ')
    return redirect(url_for('login'))

######pdfs#############
@app.route('/syl')
def syl():
    return render_template('assets/syl.pdf')

if __name__ =="__main__":
    app.run(debug=True)