from minecraft_query import MinecraftQuery

class mcstatus(MCSERVER_ADDR):

    get_status = MinecraftQuery(MCSERVER_ADDR,25565).get_rules()
    ONLINE_PLAYERS = get_status['players']
    NUM_PLAYERS = get_status['numplayers']
    MAX_PLAYERS = get_status['maxplayers']

