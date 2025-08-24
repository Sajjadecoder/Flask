from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,equal_to,Email,DataRequired
class RegisterForm(FlaskForm):
    username = StringField(label='Username',validators=[Length(min=2,max=10),DataRequired()])
    email = StringField(label='Email',validators=[Email(),DataRequired()])
    password1 = PasswordField(label='Password',validators=[Length(min=6),DataRequired()])
    password2 = PasswordField(label='Confirm Password',validators=[equal_to('password1'),DataRequired()])
    submit = SubmitField(label='Create Account')


