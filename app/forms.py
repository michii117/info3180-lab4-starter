from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_wtf.csrf import CSRFProtect


class UploadForm(FlaskForm):
    filed = FileField('Choose File: ', validators=[FileRequired(), FileAllowed(['jpg', 'png'],'Image Files Only!')])


