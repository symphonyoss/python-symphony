#!/usr/bin/env python
'''
    Purpose:
        MessageML Parser
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@joyce.nyc'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'

import logging

from bs4 import BeautifulSoup
from datetime import datetime as date


class Mml():

    def __init__(self, logger=None):
        ''' command line argument parsing '''
        self.logger = logger or logging.getLogger(__name__)

    def parse_MML(self, mml):
        ''' parse the MML structure '''
        hashes_c = []
        mentions_c = []
        soup = BeautifulSoup(mml, "lxml")
        hashes = soup.find_all('hash', {"tag": True})
        for hashe in hashes:
            hashes_c.append(hashe['tag'])
        mentions = soup.find_all('mention', {"uid": True})
        for mention in mentions:
            mentions_c.append(mention['uid'])
        msg_string = soup.messageml.text.strip()
        self.logger.debug('%s : %s : %s' % (hashes_c, mentions_c, msg_string))
        return hashes_c, mentions_c, msg_string

    def parse_msg(self, datafeed):
        ''' parse messages '''
        message_parsed = []
        for message in datafeed:
            mid = message['id']
            streamId = message['streamId']
            mstring = message['message']
            fromuser = message['fromUserId']
            timestamp = message['timestamp']
            timestamp_c = date.fromtimestamp(int(timestamp) / 1000.0)
            hashes, mentions, msg_string = self.parse_MML(mstring)
            message_broke = {'messageId': mid,
                             'streamId': streamId,
                             'fromUser': fromuser,
                             'timestamp': timestamp,
                             'timestamp_c': timestamp_c,
                             'hashes': hashes,
                             'mentions': mentions,
                             'messageStr': msg_string}
            message_parsed.append(message_broke)
        self.logger.debug(message_parsed)
        return message_parsed
