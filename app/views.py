from flask import render_template, request, url_for, redirect, flash
from sqlalchemy import exc
from app import app, db
from minecraft_query import MinecraftQuery
from mail import SignupAlert
from forms import SignupForm
from models import User
from traceback import format_exc
import fishstats


@app.route('/')
def index():
    NUMSERVERS = len(app.config['MCSERVERS'])

    return render_template('index.html',
                           NUMSERVERS=NUMSERVERS)


@app.route('/donate')
def about():
    return render_template('donate.html')


@app.route('/dynmap')
def dynmap():
    return render_template('dynmap.html')


@app.route('/forum')
def forum():
    return render_template('forum.html',
                           SITE_TITLE='Voltaire')


@app.route('/mcstatus/<MCSERVER_ADDR>/', defaults={'MCSERVER_PORT': 25565})
@app.route('/mcstatus/<MCSERVER_ADDR>/<int:MCSERVER_PORT>')
def return_mcstatus(MCSERVER_ADDR, MCSERVER_PORT):
    get_status = MinecraftQuery(MCSERVER_ADDR, MCSERVER_PORT).get_rules()
    return render_template('mcstatus.html',
                           get_status=get_status)


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)
    applicant_ip = request.environ.get('REMOTE_ADDR')
    if request.method == 'POST' and form.validate():
        user = User(form.mcuser.data,
                    form.mcemail.data,
                    form.applicant_age.data,
                    form.applicant_skills.data,
                    applicant_ip,
                    fishstats.Player(form.mcuser.data).hasBeenBanned())

        db.session.add(user)

        try:
            db.session.commit()
            tb = format_exc()
            SignupAlert(form.mcuser.data,
                        form.mcemail.data,
                        form.applicant_age.data,
                        form.applicant_skills.data,
                        applicant_ip,
                        fishstats.Player(form.mcuser.data).hasBeenBanned(),
                        tb)

        except exc.IntegrityError:
            tb = format_exc()
            SignupAlert(form.mcuser.data,
                        form.mcemail.data,
                        form.applicant_age.data,
                        form.applicant_skills.data,
                        applicant_ip,
                        fishstats.Player(form.mcuser.data).hasBeenBanned(),
                        tb)
            flash('Something is broken.', 'error')
            return redirect(url_for('signup'))

        else:
            flash('Please check your email for a response soon.', 'success')
            return redirect(url_for('signup'))

    return render_template('signup.html',
                           form=form)


@app.route('/blog')
def blog_redirect():
    return redirect('/blog')


@app.errorhandler(403)
def page_forbidden(e):
    return render_template('errorpage.html', error_code='403'), 403


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errorpage.html', error_code='404'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errorpage.html', error_code='500'), 500
