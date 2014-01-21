import urllib2
import json

from fishexc import FishbansException
ENDPOINT = 'http://www.fishbans.com/api/'

class Player(object):
    def __init__(self, player_name):
        self.player_name = player_name

    def get_bans(self):
        endpoint = ENDPOINT + 'bans/{0}/'.format(self.player_name)
        resp = urllib2.urlopen(endpoint)
        json_data = resp.read()

        data = json.loads(json_data)
        if data['success'] == True:
            return data['bans']
        else:
            raise FishbansException(data['error'])
            return data

    def queue(self):
        endpoint = ENDPOINT + 'bans/{0}/queue/'.format(self.player_name)
        resp = urllib2.urlopen(endpoint)
        json_data = resp.read()

        data = json.loads(json_data)
        if data['success'] == True:
            return True
        else:
            raise FishbansException(data['error'])
            return False

class ServicePlayer(Player):
    def __init__(self, player_name, service):
        self.player_name = player_name
        self.service = service

    def get_bans(self):
        endpoint = ENDPOINT + 'bans/{0}/{1}/'.format(self.player_name, self.service)
        resp = urllib2.urlopen(endpoint)
        json_data = resp.read()

        data = json.loads(json_data)
        if data['success'] == True:
            return data['bans']
        else:
            raise FishbansException(data['error'])
            return data

class Service(object):
    def __init__(self, service):
        self.service = service

    def get_player(self, player_name):
        return ServicePlayer(player_name, self.service)
