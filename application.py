from flask import Flask, render_template
from minecraft_query import MinecraftQuery

app = Flask(__name__)

@app.route('/')
def voltaire():
    #url_for('static', filename='css/bootstrap-responsive.min.css')
    #url_for('static', filename='js/mcstatus.js')
    servers = {'vanilla': "mc.voltaire.sh", 'ftb': "ftb.voltaire.sh", 'creative': "create.voltaire.sh"}
    numServers = len(servers)

    return render_template('index.html', site_title="Voltaire", servers=servers, numServers=numServers)

@app.route('/mcstatus/<hostname>')
def mcstatus(hostname):

    get_status = MinecraftQuery(hostname,25565).get_rules()
    onlinePlayers = get_status['players']
    numPlayers = get_status['numplayers']
    maxPlayers = get_status['maxplayers']

    return render_template('mcstatus.html', onlinePlayers=onlinePlayers, numPlayers=numPlayers, maxPlayers=maxPlayers)

if __name__ == '__main__':
    app.run()
