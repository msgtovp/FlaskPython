from flask import Flask, redirect, url_for, render_template, request, send_from_directory, send_file

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['MAX_FILE_CONTENT'] = 10240
app.config['UPLOAD_FOLDER'] = 'C:\\Users\\KCE\\Desktop\\'

@app.route("/")
@app.route("/home")
def index():
    return render_template("upload-form.html")

@app.route("/uploader", methods = ["POST"])
def file_uploader():
    note = request.files['notes']
    note.save(app.config['UPLOAD_FOLDER'] + note.filename)
    return "File Uploaded"

@app.route("/downloader")
def file_downloader():
    #return send_file(app.config["UPLOAD_FOLDER"] + "point.txt", as_attachment=True)
    return send_from_directory(app.config["UPLOAD_FOLDER"], "abstraction.txt", as_attachment=True)


if __name__ == '__main__':
    app.run(port=82)