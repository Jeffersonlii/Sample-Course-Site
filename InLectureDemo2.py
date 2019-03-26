from flask import Flask, session, redirect, url_for, escape, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app=Flask(__name__)
app.secret_key=b'abbas'
app.config['SQLALCHEMY_DATABASE_URI'] = ''
db = SQLAlchemy(app)



@app.route('/')
def index():
	if 'username' in session:
		sql1 = """
					SELECT *
					FROM marks
					where studentname='{}'""".format(session['username'])
		results = db.engine.execute(text(sql1))
		return render_template('home.html',data=results)
	else:
		return 'You are not logged in'

@app.route('/login',methods=['GET','POST'])
def login():
	if request.method=='POST':
		sql = """
			SELECT *
			FROM users
			"""
		results = db.engine.execute(text(sql))
		for result in results:
			if result['username']==request.form['username']:
				if result['password']==request.form['password']:
					session['username']=request.form['username']
					sql1 = """
						SELECT *
						FROM marks
						where studentname='{}'""".format(request.form['username'])
					results = db.engine.execute(text(sql1))
					return render_template('home.html',data=results)
		return "Incorrect UserName/Password"
	elif 'username' in session:
			sql1 = """
					SELECT *
					FROM marks
					where studentname='{}'""".format(session['username'])
			results = db.engine.execute(text(sql1))
			return render_template('home.html',data=results)
	else:
		return '''
			<form method="post">
			<p>Enter your username: <input type=text name=username>
			<p>Enter your password: <input type=password name=password>
			<p><input type=submit value=Submit>
			</form>
			'''
@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect(url_for('login'))

if __name__=="__main__":
	app.run(debug=True)