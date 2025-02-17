from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class FileModel(db.Model):
    __tablename__ = 'files'

    uid = db.Column(type_=db.String(36), unique=True, nullable=False, primary_key=True)
    original_name = db.Column(type_=db.String(255), nullable=False)
    extension = db.Column(type_=db.String(10), nullable=False)
    size = db.Column(type_=db.Integer, nullable=False)
    format = db.Column(type_=db.String(50), nullable=False)

    def __repr__(self):
        return f'<FileModel {self.original_name}>'