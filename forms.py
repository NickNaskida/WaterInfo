from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired


class LackForm(FlaskForm):
    info = StringField('marker text', validators=[DataRequired()])
    latitude = IntegerField('Latitude', validators=[DataRequired()])
    longitude = IntegerField('Longitude', validators=[DataRequired()])


class SourceForm(FlaskForm):
    info = StringField('marker text', validators=[DataRequired()])
    latitude = IntegerField('Latitude', validators=[DataRequired()])
    longitude = IntegerField('Longitude', validators=[DataRequired()])
