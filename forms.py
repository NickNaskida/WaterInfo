from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class SourceForm(FlaskForm):
    info = StringField('short info', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
