from flask import render_template, request, url_for, redirect, flash
from app import app, db
from vmail import testmail
from forms import SignupForm
from models import User, ROLE_USER, ROLE_MEMBER, ROLE_ADMIN

@app.route("/")
def index():
    testmail()
    return render_template('testmail.html')

@app.route("/signup", methods = ['GET', 'POST'])
def signup():
    form = SignupForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.mcuser.data, form.mcemail.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for signing up. Please check your email for a response soon!')
        return redirect(url_for('index'))
    return render_template('signup.html',
            title = 'Signup',
            form = form)

# @app.route("/submit_application", methods=['POST'])
# def submit_application(): 
