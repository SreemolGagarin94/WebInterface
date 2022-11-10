from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,RadioField,TextAreaField
from wtforms.validators import Length,EqualTo,DataRequired,ValidationError,InputRequired
from WebInterface.models import Users

class RegisterForm(FlaskForm):
    def validate_username(self,username_to_check):
        user =Users.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists!')

    name=StringField(label='Name',validators=[Length(min=2,max=30),DataRequired()])
    username=StringField(label='Username',validators=[Length(min=2,max=30),DataRequired()])
    password1=PasswordField(label='Password',validators=[Length(min=3),DataRequired()])
    password2=PasswordField(label='Confirm password',validators=[EqualTo('password1'),DataRequired()])
    submit=SubmitField(label='Register')

class LoginForm(FlaskForm):
    username=StringField(label='Username',validators=[DataRequired()])
    password=PasswordField(label='Password',validators=[DataRequired()])
    submit=SubmitField(label='Sign in')


class RecipientField(StringField):

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = [x.strip() for x in valuelist[0].split(',')]
        else:
            self.data = []
class sms_sendingForm(FlaskForm):
    recipients=RecipientField(label="Recipients",validators=[DataRequired()])
    originator=StringField(label="Originator",validators=[DataRequired()])
    encoding= RadioField(label='Data encoding', choices=[(1,'unicode'), (2,'text')],default=1, coerce=int,validators=[InputRequired()])
    content=TextAreaField(label="Content")
    submit=SubmitField(label="Send")