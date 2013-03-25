from minecraft_query import MinecraftQuery

class mcstatus:

    global MCSERVER_ADDR
    global MCSERVER_NAME
    query_mcserver = MinecraftQuery(MCSERVER_ADDR,25565).get_rules()

    GAME_ID = query_mcserver['game_id']
    GAMETYPE = query_mcserver['gametype']
    MOTD = query_mcserver['motd']
    MAP = query_mcserver['map']
    MAX_PLAYERS = query_mcserver['maxplayers']
    MCSERVER_PLAYERS = query_mcserver['players']
    MCSERVER_PLUGINS = query_mcserver['plugins']
    MCSERVER_RAWPLUGINS = query_mcserver['raw_plugins']
    MCSERVER_SOFTWARE = query_mcserver['software']
    MCSERVER_VERSION = query_mcserver['version']
    NUM_PLAYERS = query_mcserver['numplayers']
    ONLINE_PLAYERS = query_mcserver['players']

