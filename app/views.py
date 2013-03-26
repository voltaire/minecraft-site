from flask import render_template
from app import app

@app.route('/')
def voltaire():
    NUMSERVERS = len(MCSERVERS)

    return render_template('index.html',
            PAGE_TITLE='Dashboard',
            SITE_TITLE=SITE_TITLE, 
            MCSERVERS=MCSERVERS, 
            NUMSERVERS=NUMSERVERS)

@app.route('/about')
def about():
    return render_template('about.html', 
            SITE_TITLE=SITE_TITLE)

@app.route('/mcstatus/<MCSERVER_ADDR>/<int:MCSERVER_PORT>')
def return_mcstatus(MCSERVER_ADDR, MCSERVER_PORT):
    get_status = MinecraftQuery(MCSERVER_ADDR,MCSERVER_PORT).get_rules()
    ONLINE_PLAYERS = get_status['players']
    NUM_PLAYERS = get_status['numplayers']
    MAX_PLAYERS = get_status['maxplayers']
    return render_template('mcstatus.html', 
            MCSERVER_ADDR=MCSERVER_ADDR
            ONLINE_PLAYERS=ONLINE_PLAYERS
            NUM_PLAYERS = NUM_PLAYERS
            MAX_PLAYERS = MAX_PLAYERS)

