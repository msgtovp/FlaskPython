from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True
for each in app.config:
    print(each, "==>", app.config[each])

@app.route("/")
@app.route("/home")
def index():
    return "Home Page COntent"


if __name__ == '__main__':
    app.run()