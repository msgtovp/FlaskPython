from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    #request.cookies['auth_user']
    return "Home Page"

@app.route("/remove/cookie")
def delete_cookie():
    response = make_response("Cookie Removed")
    response.set_cookie('flask_id', max_age=0)
    return response

@app.route("/set/cookie")
def set_cookie():
    response = make_response("Cookie Created")
    #set_cookie(key, value='', max_age=None, expires=None, path='/', domain=None, secure=None, httponly=False)
    response.set_cookie('flask_id', 'secure', max_age=24*60*60)
    return response

@app.route("/get/cookie")
def get_cookie():
    #Single Cookie
    #request.cookies.get('auth_user') or request.cookies['auth_user']
    #All Cookies
    return  "Cookies" + str(request.cookies)


if __name__ == '__main__':
    app.run(debug=True)