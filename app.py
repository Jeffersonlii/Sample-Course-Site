from flask import Flask, session, redirect, url_for, escape, request, render_template 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)
app.secret_key=b'supersecret1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///assignment3.db'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0#avoids caching
db = SQLAlchemy(app)
@app.route('/',methods=['GET','POST'])
@app.route('/login',methods=['GET','POST'])
def login():

    if 'name' in session:
        return redirect(url_for('home')) 

    elif request.method=='POST':
        if 'login' in request.form:#if login button is pressed
            
            results = db.engine.execute(text("select * from users"))
            for result in results: 
                if result['username'] == request.form['username']:
                    if result['password'] == request.form['password']:
                        fillSession(result)
                        return redirect(url_for('home')) 
                    else: # if pass isnt correct, go back
                        return render_template('index.html',alert="pass")   
            return render_template('index.html',alert="pass")
        elif 'newReg' in request.form:
            #if newred is pressed
            u = request.form['usernamereg']
            p = request.form['passwordreg']
            t = request.form['pulldown']
            if u == "" or p == "" or t == '0':
                return render_template('index.html',alert="insuf")
            insert("ACCOUNT",username=u,password=p,type=t)    
            return render_template('index.html')

    elif request.method=='GET':
        return render_template('index.html')

def fillSession(result):
    if 'username' not in session:
        session['username'] = result['username']
        session['type'] = result['type']

def query(requested_data):
    # returns bundle of requested data
    # could request: 
    # instructor: feedback, all student grades
    # students : students grades
    data = []# package of data depending on requested
    if session['type'] == 'INSTRUCTOR':
        if requested_data == "FEEDBACK":
            sql = """
            select feedback.username,reviews from users 
            left join feedback on users.username == feedback.username
            where users.username == "{}" """.format(session['username'])
            data = db.engine.execute(text(sql))
        elif requested_data == "ALLGRADES":#requesting all student grades
            data = db.engine.execute(text('select * from grades'))
        elif requested_data == "REMARKS":
            data = db.engine.execute(text('select * from remarks'))

    else:# else, its a student requesting his grades
        if requested_data == "MYGRADES":
            sql = """
            select username, a1,a2,a3,q1,q2,q3,q4,midterm,final from grades 
            where username == "{}" """.format(session['username'])
            data = db.engine.execute(text(sql))
        if requested_data == "INSTRUCTORNAMES":
            sql = """select username from users
                    where type == "INSTRUCTOR" """
            data = db.engine.execute(text(sql))
    return data

def insert(insertionType,paragraph=None,password=None,type=None,username=None):
    #types - ACCOUNT, FEEDBACK, REMARK
    #if insertionType == "ACCOUNT":
 
    
    
    
    return


######similar pages####### V
@app.route('/CWork')
def CWork():
    return render_template('common/CWork.html', data= session['username'])

@app.route('/instructor')
def instructor():
    return render_template('common/instructor.html', data= session['username'])

@app.route('/Ohour')
def c():
    return render_template('common/Ohour.html', data= session['username'])

#####instructor pages##### V
@app.route('/myFeedBack')#need query info
def myFeedBack():
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
        return render_template('instructor/myFeedBack.html', data=lstF, name = session['username'])

@app.route('/gradesAll',methods=['GET','POST'])#need query info
def gradesAll():
    if request.method=='POST':#update grades

        students = db.engine.execute(text('''select username from users
                    where type == "STUDENT" '''))
        
        for student in students:
            sql = """select q1,q2,q3,q4,a1,a2,a3,midterm,
            final from grades where username = "{}"
            """.format(student[0])
            grades = db.engine.execute(text(sql))
            for row in grades:
                for count, grade in enumerate(row):
                    if(request.form[student[0]+" "+str(count)] != str(grade)):
                        pass
                        #replace the value in the db with request.form[student[0]+" "+str(count)]
                    
                    
                    
        return render_template('instructor/gradesAll.html', data=query("ALLGRADES"), name = session['username'])
    else:
        return render_template('instructor/gradesAll.html', data=query("ALLGRADES"), name = session['username'])

@app.route('/myRemarks')
def myRemarks():
    return render_template('instructor/myRemarks.html', data=query("REMARKS"), name = session['username'])


#####student pages##### V
@app.route('/Feedback') 
def Feedback():
    return render_template('student/Feedback.html',data=query("INSTRUCTORNAMES"), name= session['username'])

@app.route('/gradesMy')#need query info
def gradesMy():
    data = query("MYGRADES")
    for i in data:
        return render_template('student/gradesMy.html', data=i, name =session['username'] )

##### home ####### V
@app.route('/home')
def home():
    if session['type'] == 'INSTRUCTOR':
        return render_template('instructor/homeInstructor.html', data= session['username'])
    else:
        return render_template('student/homeStudent.html', data = session['username'])

######log out############
@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')

    if 'type' in session:
        session.pop('type')
    
    return redirect(url_for('login')) 

if __name__ =="__main__":
    #SQLALCHEMY_TRACK_MODIFICATIONS = False
    app.run(host="localhost",port=5000,debug=True)