from flask import Flask, render_template, request

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


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        html = """<div><b>Username:</b>**userval**</div>\n<div><b>Password:</b>**passval**</div>"""
        return html.replace("**userval**", request.form["user"]).replace("**passval**", request.form["pass"])


if __name__ == '__main__':
    app.run(debug=True)