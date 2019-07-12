from flask import Flask,render_template,request,redirect,url_for,session


app=Flask(__name__)
app.secret_key='abc'
@app.route('/')
def layout() :
	return render_template("lay.html")

@app.route('/home2')
def home() :
	return render_template("home2.html")

@app.route('/aboutme')
def about() :
	return render_template("aboutme.html")

@app.route('/contact')
def contact() :
	return render_template("contact.html")


@app.route('/login',methods=['GET','POST'])

def login() :

	if request.method == 'POST' :
		users={"user1":"123","user2":"234","user3":"1234","user4":"2345"}
		username=request.form['username']
		password=request.form['password']

		if username not in users :
			return " User doesnot exist.Go back and enter a valid username "
		if users[username]!=password :
			return " Password doesnot match.Go back and reenter the password"

		session['username']=username
		return redirect(url_for('home'))
	return redirect(url_for('home'))

@app.route('/logout')

def logout() :
	session.clear()
	return redirect(url_for('home'))

app.run(debug=True)
