from flask import Flask, session, redirect, url_for, escape, request, render_template 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)
app.secret_key=b'supersecret1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/db.db'
db = SQLAlchemy(app)
data = None
@app.route('/',methods=['GET','POST'])
@app.route('/login',methods=['GET','POST'])
def login():
    if 'email' in session:
        results = db.engine.execute(text("select * from users"))
        for result in results: 
            if result['email'] == session['email']:
                return query(result)
        

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
    if result['type'] == "INSTRUCTOR":
        sql = """
            select name,reviews from users 
            left join feedback on users.email == feedback.email
            where users.email == {}""".format(result['email'])
        session['email'] = result['email']
        session['typ'] = result['type']
        #returns instructor name and reviews
        result = db.engine.execute(text(sql))

    else:# if user is a student
        sql = """
            select name, a1,a2,a3,q1,q2,q3,q4,midterm,final from users 
            left join grades 
            on users.studentNumber == grades.studentNumber
            where type != "INSTRUCTOR" and users.email =={}
            """.format(result['email'])
        session['email'] = result['email']
        session['typ'] = result['type']
        result = db.engine.execute(text(sql))
        

    return redirect(url_for('goToHome'))


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
    return render_template('myFeedBack.html',data=session['data'])

@app.route('/gradesAll')
def f():
    return render_template('gradesAll.html',data=session['data'])

#####student pages##### V
@app.route('/Feedback')
def g():
    return render_template('Feedback.html')

@app.route('/gradesMy')
def i():
    return render_template('gradesMy.html',data=session['data'])

##### home ####### V
@app.route('/home')
def goToHome():
    if session['typ'] == 'INSTRUCTOR':
        return render_template('homeInstructor.html',data=session['data'])
    else:
        return render_template('homeStudent.html',data=session['data'])

######log out############
@app.route('/logout')
def logout():
    session.pop('email')
    session.pop('data')
    session.pop('typ')
    return redirect(url_for('login'))

######pdfs#############
@app.route('/syl')
def syl():
    return render_template('assets/syl.pdf',data=session['data'])

if __name__ =="__main__":
    app.run(debug=True)