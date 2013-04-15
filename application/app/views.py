from flask import render_template, request, url_for, redirect, flash
from sqlalchemy import exc
from app import app, db
from minecraft_query import MinecraftQuery
from vmail import testmail, SignupAlert
from forms import SignupForm
from models import User
from traceback import format_exc

@app.route('/')
def index():
    NUMSERVERS = len(app.config['MCSERVERS'])

    return render_template('index.html',
            NUMSERVERS=NUMSERVERS)

@app.route('/dash')
def dash():
    NUMSERVERS = len(app.config['MCSERVERS'])

    return render_template('dash.html',
            NUMSERVERS=NUMSERVERS)

@app.route('/donate')
def about():
    return render_template('donate.html')

@app.route('/dynmap')
def dynmap():
    return render_template('dynmap.html')

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
            tb = format_exc()
            SignupAlert(form.mcuser.data,
                        form.mcemail.data,
                        userAddr,
                        tb)
            flash('Oh no! It looks like there\'s something wrong with your information. Admins have been contacted.', 'error')
            return redirect(url_for('signup'))

        else:
            flash('Thanks for signing up. Please check your email for a response soon!', 'success')
            return redirect(url_for('signup'))

    return render_template('signup.html',
            form = form)

@app.errorhandler(403)
def page_forbidden(e):
    return render_template('403.html'), 403

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500 

