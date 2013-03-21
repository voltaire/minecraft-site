from flask import Flask, render_template
from minecraft_query import MinecraftQuery

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('application.cfg', silent=True)

@app.route('/')
def voltaire():
    NUMSERVERS = len(MCSERVERS)

    return render_template('index.html', PAGE_TITLE=PAGE_TITLE, SITE_TITLE=SITE_TITLE, MCSERVERS=MCSERVERS, NUMSERVERS=NUMSERVERS)

@app.route('/about')
def about():
    return render_template('about.html', SITE_TITLE=SITE_TITLE)

@app.route('/mcstatus/<hostname>')
def mcstatus(MCSERVER_ADDR):

    get_status = MinecraftQuery(MCSERVER_ADDR,25565).get_rules()
    ONLINE_PLAYERS = get_status['players']
    NUM_PLAYERS = get_status['numplayers']
    MAX_PLAYERS = get_status['maxplayers']

    return render_template('mcstatus.html', ONLINE_PLAYERS=ONLINE_PLAYERS, NUM_PLAYERS=NUM_PLAYERS, MAX_PLAYERS=MAX_PLAYERS)

if __name__ == '__main__':
    app.run()
