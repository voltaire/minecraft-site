from flask import Flask, render_template
from minecraft_query import MinecraftQuery

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('application.cfg', silent=True)

@app.route('/')
def voltaire():
    NUMSERVERS = len(MCSERVERS)

    return render_template('index.html', site_title=SITE_TITLE, servers=MCSERVERS, numServers=NUMSERVERS)

@app.route('/mcstatus/<hostname>')
def mcstatus(hostname):

    get_status = MinecraftQuery(hostname,25565).get_rules()
    onlinePlayers = get_status['players']
    numPlayers = get_status['numplayers']
    maxPlayers = get_status['maxplayers']

    return render_template('mcstatus.html', onlinePlayers=onlinePlayers, numPlayers=numPlayers, maxPlayers=maxPlayers)

if __name__ == '__main__':
    app.run()
