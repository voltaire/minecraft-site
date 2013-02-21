from flask import Flask, render_template
from minecraft_query import MinecraftQuery

app = Flask(__name__)

@app.route('/')
def voltaire():
    #url_for('static', filename='css/bootstrap-responsive.min.css')
    #url_for('static', filename='js/mcstatus.js')

    return render_template('index.html')

@app.route('/mcstatus/')
def mcstatus():

    ftbPlayers = MinecraftQuery("ftb.voltaire.sh",25565).get_rules()['players']
    ftbNumPlayers = MinecraftQuery("ftb.voltaire.sh",25565).get_rules()['numplayers']

    vanillaPlayers = MinecraftQuery("mc.voltaire.sh",25565).get_rules()['players']
    vanillaNumPlayers = MinecraftQuery("mc.voltaire.sh",25565).get_rules()['numplayers']

    return render_template('derp.html', vanillaPlayers=vanillaPlayers, ftbPlayers=ftbPlayers, ftbNumPlayers=ftbNumPlayers, vanillaNumPlayers=vanillaNumPlayers)

@app.route('/vnstat/')
def vnstat():
    return render_template('vnstat.html')

"""@app.route('/vnstat/')
def vnstat():

    vnstat_main = vnstati("-s", i="em0", o="-")
    vnstat_hourly = vnstati("-s", "-h", i="em0", o="-")
    vnstat_daily = vnstati("-s", "-d", i="em0", o="-")
    vnstat_top10 = vnstati("-s", "-t", i="em0", o="-")
    vnstat_monthly = vnstati("-s", "-m", i="em0", o="-")

    return render_template('vnstat.html', vnstat_main=vnstat_main, vnstat_hourly=vnstat_hourly, vnstat_daily=vnstat_daily, vnstat_top10=vnstat_top10, vnstat_monthly=vnstat_monthly)

@app.route('/derp/')
def serve_img():
    vnstat_main = vnstati("-s", i="em0", o="-")
    sup = open("vnstat/vnstat.png","wb")
    mayne = sys.stdout.write( "Content-type: image/png\r\n\r\n" + file("vnstat/vnstat.png","rb").read() )
    return "derp"
"""

if __name__ == '__main__':
    app.run()
