import urllib2
import json

from fishexc import FishbansException
ENDPOINT = 'http://www.fishbans.com/api/'


class Player(object):
    """
    Class for getting stat info on a specific player.
    """
    def __init__(self, player_name):
        self.player_name = player_name

    def get_stats(self):
        endpoint = ENDPOINT + 'stats/{0}/'.format(self.player_name)
        resp = urllib2.urlopen(endpoint)
        json_data = resp.read()

        data = json.loads(json_data)
        if data['success'] is True:
            return data['stats']
        else:
            raise FishbansException(data['error'])
            return data

    def hasBeenBanned(self):

        totalBans = self.get_stats()['totalbans']

        if totalBans == 0:
            return False

        if totalBans != 0:
            return True

    def queue(self):
        endpoint = ENDPOINT + 'stats/{0}/queue/'.format(self.player_name)
        resp = urllib2.urlopen(endpoint)
        json_data = resp.read()

        data = json.loads(json_data)
        if data['success'] is True:
            return True
        else:
            raise FishbansException(data['error'])
            return False


class ServicePlayer(Player):
    def __init__(self, player_name, service):
        self.player_name = player_name
        self.service = service

    def get_stats(self):
        endpoint = ENDPOINT + 'stats/{0}/{1}/'.format(
            self.player_name, self.service)
        resp = urllib2.urlopen(endpoint)
        json_data = resp.read()

        data = json.loads(json_data)
        if data['success'] is True:
            return data['stats']
        else:
            raise FishbansException(data['error'])
            return data


class Service(object):
    def __init__(self, service):
        self.service = service

    def get_player(self, player_name):
        return ServicePlayer(player_name, self.service)
