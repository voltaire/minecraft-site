from flask import Flask, render_template
from minecraft_query import MinecraftQuery

app = Flask(__name__)

@app.route('/')
def voltaire():
    #url_for('static', filename='css/bootstrap-responsive.min.css')
    #url_for('static', filename='js/mcstatus.js')

    return render_template('index.html', site_title="Voltaire")

@app.route('/mcstatus/')
def mcstatus():

    ftbPlayers = MinecraftQuery("ftb.voltaire.sh",25565).get_rules()['players']
    ftbNumPlayers = MinecraftQuery("ftb.voltaire.sh",25565).get_rules()['numplayers']

    vanillaPlayers = MinecraftQuery("mc.voltaire.sh",25565).get_rules()['players']
    vanillaNumPlayers = MinecraftQuery("mc.voltaire.sh",25565).get_rules()['numplayers']

    return render_template('mcstatus.html', vanillaPlayers=vanillaPlayers, ftbPlayers=ftbPlayers, ftbNumPlayers=ftbNumPlayers, vanillaNumPlayers=vanillaNumPlayers)

@app.route('/vnstat/')
def vnstat():
    return render_template('vnstat.html')

if __name__ == '__main__':
    app.run()
