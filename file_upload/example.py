from flask import Flask, request, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

from werkzeug.utils import secure_filename


app=Flask(__name__)
app.config['SALALCHEMY_DATABASE_URI']='sqlite:///upload.db'
db=SQLAlchemy(app)

# UPLOAD_FOLDER = '/home/vguggilam/Music/img/uploads'
# ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv'])

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

class FileContents(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(300))
    data=db.Column(db.LargeBinary)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
       
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="abc.html" method="post" enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload></p>
         </form>
    </html>
    '''


