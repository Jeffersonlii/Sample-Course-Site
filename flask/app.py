from flask import Flask, session, redirect, url_for, escape, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://// adress of db'
db = SQLAlchemy(app)

@app.route('/',methods=['GET','POST'])
@app.route('/login',methods=['GET','POST'])
def login():
    if 'studentNumber' in session:
        return render_template('home.html',data=session['studentNumber'])

    elif request.method=='POST':
        sql = """select * from studentNumber"""
        results = db.engine.execute(text(sql))
        for result in results:
            if result['studentNumber'] == request.form['studentNumber']:
                if result['password'] == request.form['password']:
                    session['studentNumber'] = request.form['studentNumber']
                    return render_template('home.html',data=result['studentNumber'])


    elif request.method=='GET':
        return render_template('index.html')


def logout():
    session.pop('studentNumber')

if __name__ =="__main__":
    app.run(debug=True)