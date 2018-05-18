from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("landing.html")

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return "This is contact page"

@app.route("/success")
def login_success():
    return "Login Success"

@app.route("/error")
def login_error():
    return "Login Error"

@app.route("/login", methods=['GET', 'POST'])
def login():
    print(request.headers)
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        req = {'username': request.form["user"], 'password': request.form["pass"]}
        data = {'username': 'steve', 'password': 'jobs'}
        if data == req:
            return redirect(url_for('login_success'))
        else:
            return redirect(url_for('login_error'))

@app.route("/users/all")
def get_users():
    users = [
        {'user':'guido', 'pass': 'rossum', 'fullname': 'Guido Van Rossum'},
        {'user':'james', 'pass': 'gosling', 'fullname': 'James Gosling'},
        {'user':'frank', 'pass': 'edust', 'fullname': 'EdFrank'},
        {'user':'chrish', 'pass': 'worth', 'fullname': 'Chrish Worth'},
        {'user':'patrick', 'pass': 'naughton', 'fullname': 'Patrick Naughton'}
    ]
    return jsonify(users)

@app.errorhandler(404)
def test(e):
    return "not found", 404

@app.route("/getdata")
def get_data():
    print(request.headers)
    print(request.headers["Accept"])
    if request.headers["Accept"] == "application/json":
        return '{"message": "Data to be transfered"}', 200, {"Content-Type": "application/json"}
    else:
        return "<h2>Data to be transfered</h2>", 200, {"Content-Type": "text/html"}

if __name__ == '__main__':
    app.run(debug=True)