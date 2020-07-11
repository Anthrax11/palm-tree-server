from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegisterUser(FlaskForm):
    username = StringField('Username', validators = [Length(min=4, max=25)])
    email = StringField('Email Address', validators = [Length(min=6, max=120), Email()])
    password = PasswordField('New Password', validators = [
        DataRequired(),
        EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Submit')