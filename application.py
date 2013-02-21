from flask import Flask, render_template
from minecraft_query import MinecraftQuery

app = Flask(__name__)

@app.route('/')
def voltaire():
    #url_for('static', filename='css/bootstrap-responsive.min.css')
    #url_for('static', filename='js/mcstatus.js')

    return render_template('index.html', site_title="Voltaire")

@app.route('/mcstatus/<hostname>')
def mcstatus(hostname):

    onlinePlayers = MinecraftQuery(hostname,25565).get_rules()['players']
    numPlayers = MinecraftQuery(hostname,25565).get_rules()['numplayers']

    return render_template('mcstatus.html', onlinePlayers=onlinePlayers, numPlayers=numPlayers)

@app.route('/vnstat/')
def vnstat():
    return render_template('vnstat.html')

if __name__ == '__main__':
    app.run()
