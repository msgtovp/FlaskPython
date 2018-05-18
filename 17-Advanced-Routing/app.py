from flask import Flask, redirect, url_for, render_template, request, send_from_directory, send_file

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/users")
def index():
    return "Users Content"

#@app.route("/users/<string:username>")
#exclude forward slashes
@app.route("/users/<username>")
def show_user(username):
    return "Username: " + username

@app.route("/add/<int:value1>/<int:value2>")
def math_add(value1, value2):
    return "Result: " + str(value1 + value2)

@app.route("/sub/<float:value1>/<float:value2>")
def math_sub(value1, value2):
    return "Result: " + str(value1 - value2)

#includes forward slashes
@app.route("/url/<path:red>")
def url_path(red):
    return "Path Scanned: " + str(red)

@app.route("/hex/<uuid:data>")
def hex_hand(data):
    return "Unicode Data:" + str(data)

if __name__ == '__main__':
    app.run()