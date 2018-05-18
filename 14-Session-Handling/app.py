from flask import Flask, session, redirect, url_for

app = Flask(__name__)
app.config['DEBUG'] = True
app.config["SECRET_KEY"] = "abjhfghjgkhljlhg"

@app.route("/")
@app.route("/home")
def index():
    if 'test_user' in session:
        user = session['test_user']
    else:
        user = 'Guest'
    if 'admin_user' in session:
        admin = session['admin_user']
    else:
        admin = 'Dust'
    return "Home Page Content:" + user + admin


@app.route("/make_login_success")
def login_success():
    session['test_user'] = 'Steve'
    session['admin_user'] = 'James'
    return redirect(url_for('index'))

@app.route("/logout")
def logout():
    #del session['test_user']
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()