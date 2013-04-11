from flask import render_template, request, url_for, redirect, flash
from sqlalchemy import exc
from app import app, db
from minecraft_query import MinecraftQuery
from vmail import testmail
from forms import SignupForm
from models import User

@app.route('/')
def index():
    NUMSERVERS = len(app.config['MCSERVERS'])

    return render_template('index.html',
            PAGE_TITLE='Home',
            SITE_TITLE='Voltaire',
            NUMSERVERS=NUMSERVERS)

@app.route('/dash')
def dash():
    NUMSERVERS = len(app.config['MCSERVERS'])

    return render_template('dash.html',
            PAGE_TITLE='Dashboard',
            SITE_TITLE='Voltaire',
            NUMSERVERS=NUMSERVERS)

@app.route('/donate')
def about():
    return render_template('donate.html', 
            SITE_TITLE='Voltaire')

@app.route('/mcstatus/<MCSERVER_ADDR>/<int:MCSERVER_PORT>')
def return_mcstatus(MCSERVER_ADDR, MCSERVER_PORT):
    get_status = MinecraftQuery(MCSERVER_ADDR,MCSERVER_PORT).get_rules()
    return render_template('mcstatus.html', 
            get_status = get_status)

@app.route("/signup", methods = ['GET', 'POST'])
def signup():
    form = SignupForm(request.form)
    userAddr = request.environ.get('REMOTE_ADDR')
    if request.method == 'POST' and form.validate():
        user = User(form.mcuser.data, form.mcemail.data, userAddr)
        db.session.add(user)

        try:
            db.session.commit()

        except exc.IntegrityError:
            flash('Oh no! It looks like there\'s something wrong with your information. Please contact an admin.', 'error')
            return redirect(url_for('signup'))

        else:
            flash('Thanks for signing up. Please check your email for a response soon!', 'success')
            return redirect(url_for('signup'))

    return render_template('signup.html',
            title = 'Signup',
            form = form)

