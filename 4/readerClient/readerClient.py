import urllib2
import json

class readerClient:

    def __init__(self, host='0.0.0.0', url='/stats', eventTypes=['A', 'C', 'B', 'Y', 'X', 'Z']):
        self.host=host
        self.url=url
        self.eventTypes = eventTypes

    def getCounts(self):
        response = urllib2.urlopen('http://' + self.host + self.url)
        decodedJson = json.load(response)
        return decodedJson

    def getLatestEvents(self):
        latestEvents = {}
        for event in self.eventTypes:
            latestEvents[event] = self.getLatestEventOfType(event)
        return latestEvents


    def getLatestEventOfType(self, eventType):
        response = urllib2.urlopen('http://' + self.host + self.url + '/' + eventType)
        decodedJson = json.load(response)
        return decodedJson
