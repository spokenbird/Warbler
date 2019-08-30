from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, HiddenField
from wtforms.validators import DataRequired, Email, Length, Optional, URL


class MessageForm(FlaskForm):
    """Form for adding/editing messages."""

    text = TextAreaField('text', validators=[DataRequired()])


class UserAddForm(FlaskForm):
    """Form for adding users."""

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=6)])
    image_url = StringField('(Optional) Image URL')


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])


class UserEdit(FlaskForm):
    """Form for editing User Profile."""

    username = StringField("Username", validators=[Optional()])
    email = StringField("Email", validators=[Email()])
    image_url = StringField("Profile Image", validators=[Optional()])
    header_image_url = StringField("Banner Image", validators=[Optional()])
    bio = TextAreaField("Bio", validators=[Optional()])
    password = PasswordField("Password", validators=[DataRequired(),
                                                     Length(min=6)])
