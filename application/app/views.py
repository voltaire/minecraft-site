from flask import render_template
from app import app
from minecraft_query import MinecraftQuery

@app.route('/')
def voltaire():
    NUMSERVERS = len(app.config['MCSERVERS'])
    """
    d['name'] for d in app.config['MCSERVERS']:
        try:
            MCSERVER_NAME.append(d)

        except NameError:
            MCSERVER_NAME = [d]

   dd['hostname'] for dd in app.config['MCSERVERS']:
       try:
           MCSERVER_ADDR.append(dd)

       except NameError:
           MCSERVER_NAME = [dd]
    """

    return render_template('index.html',
            PAGE_TITLE='Dashboard',
            SITE_TITLE='Voltaire',
            NUMSERVERS=NUMSERVERS)

@app.route('/about')
def about():
    return render_template('about.html', 
            SITE_TITLE='Voltaire')

@app.route('/mcstatus/<MCSERVER_ADDR>/<int:MCSERVER_PORT>')
def return_mcstatus(MCSERVER_ADDR, MCSERVER_PORT):
    get_status = MinecraftQuery(MCSERVER_ADDR,MCSERVER_PORT).get_rules()
    """
    ONLINE_PLAYERS = get_status['players']
    NUM_PLAYERS = get_status['numplayers']
    MAX_PLAYERS = get_status['maxplayers']
    """
    return render_template('mcstatus.html', 
            get_status = get_status)

