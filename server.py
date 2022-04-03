from flask import Flask, redirect, url_for, render_template, session, request
app = Flask(__name__)
app.secret_key = "what the key"
@app.route("/login",methods = ['GET', 'POST'])
def login():
    session["password"] = "admin"
    if request.method == 'POST':
        if request.form["password"]==session["password"]:
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        else:
            return render_template("login.html",err="Wrong Password")
    return render_template("login.html")

@app.route("/")
def index():
    if 'username' in session:
        username = session['username']
        msg = "you are logged in as: "+ username
        return render_template("home.html", msg=msg)
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host="localhost", debug=True)