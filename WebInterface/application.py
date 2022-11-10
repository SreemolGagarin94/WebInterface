from flask import render_template, request,url_for,flash,redirect
from pydantic import ValidationError
from WebInterface import app,db,login_manager
from WebInterface.models import Users
from WebInterface.forms import RegisterForm,LoginForm,sms_sendingForm
from WebInterface.sms_api import sendSMS
from flask_login import login_user


@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form=RegisterForm()
        
    if request.method == 'POST':
        if form.validate_on_submit():
            name = form.name.data 
            username = form.username.data 
            password1 = form.password1.data
            password2 = form.password2.data 
            user = Users(name=name, username=username, password=password1)
            db.session.add(user)
            db.session.commit()
            flash('Registered successfully.')
            return redirect(url_for('login'))
        if form.errors != {}:
            for err_msg in form.errors.values():
                flash(f'Error :{err_msg}',category='danger')

    return render_template('register.html',form=form)
    
    
@app.route('/login',methods=['GET','POST'])
def login(): 
    form=LoginForm()
    if request.method == 'GET':
        return render_template('login.html',form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user_name=form.username.data
            password=form.password.data
            attempted_user= Users.query.filter_by(username=user_name).first()
            if attempted_user and password==attempted_user.password:
                login_user(attempted_user)
                return redirect(url_for('send_sms'))
            else:
                flash('Invalid username or password')
                form=LoginForm()
                return redirect(url_for('login'))


@app.route('/send_sms',methods=['GET','POST'])
def send_sms():
    form=sms_sendingForm()
    if request.method=='GET':
        return render_template('smsUI.html',form=form)
    if request.method=='POST':
        print(form.recipients.data)
        if form.validate_on_submit():
            sendSMS(form)
            flash('SMS has been sent!')
            return redirect(url_for('send_sms'))
