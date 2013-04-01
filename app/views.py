from flask import render_template
from app import app
from vmail import testmail
from forms import SignupForm

@app.route("/")
def index():
    testmail()
    return render_template('testmail.html')

@app.route("/signup", methods = ['GET', 'POST'])
def signup():
    form = SignupForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.mcuser.data, form.mcemail.data)
        db_session.add(user)
        flash('Thanks for signing up. Please check your email for a response soon!')
        return redirect(url_for('index'))
    return render_template('signup.html',
            title = 'Signup',
            form = form)

# @app.route("/submit_application", methods=['POST'])
# def submit_application(): 
