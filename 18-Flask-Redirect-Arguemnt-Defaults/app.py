from flask import Flask, redirect, url_for, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/users", defaults={'username': 'Guest'})
@app.route("/users/<username>")
def index(username):
    return "Users Content " + username

@app.route("/find/<user>")
def show_user(user):
    return redirect(url_for('index', username=user + ' user found'))


if __name__ == '__main__':
    app.run()