from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    return render_template("landing.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/search")
def search():
    query = request.args["q"]
    return "<b>Search Routing:</b>" + query

if __name__ == '__main__':
    app.run(debug=True)
    #type the url http://127.0.0.1:5000/search?q=URL+Query+String