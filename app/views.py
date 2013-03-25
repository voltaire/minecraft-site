from flask import render_template
from app import app
import mcstatus

@app.route('/')
def voltaire():
    NUMSERVERS = len(MCSERVERS)

    return render_template('index.html', PAGE_TITLE='Dashboard', SITE_TITLE=SITE_TITLE, MCSERVERS=MCSERVERS, NUMSERVERS=NUMSERVERS)

@app.route('/about')
def about():
    return render_template('about.html', SITE_TITLE=SITE_TITLE)

@app.route('/mcstatus/<MCSERVER_ADDR>')
def mcstatus(MCSERVER_ADDR):

    return render_template('mcstatus.html')

