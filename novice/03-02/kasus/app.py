import os
from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def fileFrontPage():
    return render_template('upload.html')

@app.route("/actionUpload", methods=['POST'])
def handleFileUpload():
    if 'photo' in request.files:
        photo = request.files['photo']
        if photo.filename != '':            
            photo.save(os.path.join('<upload_dir>', photo.filename))
    return redirect(url_for('fileFrontPage'))

if __name__ == '__main__':
    app.run()     