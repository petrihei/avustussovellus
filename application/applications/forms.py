from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField, validators


class ApplicationForm(FlaskForm):
    name = StringField("Application name", [validators.Length(min=2, max=50)])
    definition = TextAreaField("Definition", [validators.Length(min=10, max=500)])
    sum = FloatField("Sum", [validators.NumberRange(
        min=1, max=10000, message=None)])

    class Meta:
        csrf = False
