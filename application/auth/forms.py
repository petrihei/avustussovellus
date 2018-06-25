from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators, Form, BooleanField


class LoginForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=3)])
    password = PasswordField("Password", [validators.Length(min=5)])

    class Meta:
        csrf = False


class RegistrationForm(Form):
    name = StringField('Name', [validators.Length(min=2, max=35)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('New Password', [validators.Length(min=4, max=25),
    validators.DataRequired()])


class ModificationForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=3)])
    password = PasswordField("Password", [validators.Length(min=5)])

    class Meta:
        csrf = False
