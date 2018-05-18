from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return "<h1>Hello Welcome to Flask Application<h1>"

@app.route("/about")
def about():
    return "This is about page"

@app.route("/contact")
def contact():
    return "This is contact page"

if __name__ == '__main__':
    app.run(debug=True)