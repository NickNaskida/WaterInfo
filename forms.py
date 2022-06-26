from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class SourceForm(FlaskForm):
    info = StringField('marker title', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
