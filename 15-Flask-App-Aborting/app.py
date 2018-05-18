from flask import Flask, session, redirect, url_for, abort

app = Flask(__name__)
app.config['DEBUG'] = True
app.config["SECRET_KEY"] = "abjhfghjgkhljlhg"

@app.route("/")
@app.route("/home")
def index():
    return "<h1>Home Page Content</h1><div>\
    <a href='/profile'>Check Profile</a>"

@app.route("/profile")
def get_profile():
    if 'test_user' in session:
        user = session['test_user']
    else:
        abort(401)
    return "<B>User Logged:</B>" + user


@app.route("/set_profile")
def login_success():
    session['test_user'] = 'Steve'
    return redirect(url_for('get_profile'))


if __name__ == '__main__':
    app.run()