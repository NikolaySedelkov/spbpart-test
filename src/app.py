from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import uuid
#from models.file import FileModel
from config.db import ConfigDB
from sqlalchemy.orm import DeclarativeBase

app = Flask(__name__)
#app.config.from_object(ConfigDB)

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(app, model_class=Base)

class FileModel(db.Model):
    __tablename__ = 'files'

    uid = db.Column(type_=db.String(36), unique=True, nullable=False, primary_key=True)
    original_name = db.Column(type_=db.String(255), nullable=False)
    extension = db.Column(type_=db.String(10), nullable=False)
    size = db.Column(type_=db.Integer, nullable=False)
    format = db.Column(type_=db.String(50), nullable=False)

    def __repr__(self):
        return f'<FileModel {self.original_name}>'


print(ConfigDB.SQLALCHEMY_DATABASE_URI)

CORS(app)

@app.route('/')
def index():
    return render_template('form-file-loading.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    files = request.files.getlist('file')  # Получаем список файлов
    if not files:
        return jsonify({"error": "No files selected"}), 400


    uploaded_files = []

    for file in files:

        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        if file:
            file_uid = str(uuid.uuid4())
            filename = secure_filename(file.filename)
            file_extension = os.path.splitext(filename)[1]
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_uid + file_extension)
            file.save(file_path)

            file_size = os.path.getsize(file_path)
            file_format = file.content_type

            new_file = FileModel(
                uid=file_uid,
                original_name=filename,
                extension=file_extension,
                size=file_size,
                format=file_format
            )

            db.session.add(new_file)
            db.session.commit()

            return jsonify({
                "uid": file_uid,
                "original_name": filename,
                "extension": file_extension,
                "size": file_size,
                "format": file_format
            }), 201
        return jsonify({"error": "File type not allowed"}), 400
    
    return jsonify(uploaded_files), 201

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    with app.app_context():
        db.create_all()
    app.run(debug=True)