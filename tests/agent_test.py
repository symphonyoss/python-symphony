#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        Unit Tests for Agent Methods
            - remove_control_characters
            - test_echo
            - create_datafeed
            - read_datafeed
            - send_message
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@joyce.nyc'
__copyright__ = 'Copyright 2017, Symphony Communication Services LLC'

import httpretty
import json
import unittest
import symphony


@httpretty.activate
class Agent_tests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(Agent_tests, self).__init__(*args, **kwargs)
        self.__uri__ = "http://fake.pod/"
        self.__session__ = "sessions"
        self.__keymngr__ = "keys"
        self.agent = symphony.Agent(self.__uri__, self.__session__, self.__keymngr__)

    def test_test_echo(self):
        ''' test agent.test_echo'''
        # register response
        httpretty.register_uri(httpretty.POST, self.__uri__ + "agent/v1/util/echo",
                               body='{"message": "test string"}',
                               status=200,
                               content_type='text/json')
        # run test query
        status_code, response = self.agent.test_echo('test string')
        response = json.loads(response)
        # verify return
        assert status_code == 200
        assert response['message'] == "test string"

    def test_create_datafeed(self):
        ''' test agent.create_datafeed '''
        # register response
        httpretty.register_uri(httpretty.POST, self.__uri__ + "agent/v1/datafeed/create",
                               body='{ "id": 78910 }',
                               status=200,
                               content_type='text/json')
        # run test query
        status_code, response = self.agent.create_datafeed()
        # verify return
        assert status_code == 200
        assert response == 78910

    def test_read_datafeed(self):
        ''' test agent.read_datafeed '''
        # register response
        httpretty.register_uri(httpretty.GET, self.__uri__ + "agent/v1/datafeed/datafeed_id/read",
                               body='[{"id": "9zJTiQBL98ZEPAkvtjcweH___qr9auZ9dA", \
                                       "timestamp": "1464627173769", \
                                       "v2messageType": "V2Message", \
                                       "streamId": "thread_id", \
                                       "message": "test string 1", \
                                       "attachments": [], \
                                       "fromUserId": 123456 \
                                      },\
                                      {"id": "9zJFGHJGHGHGHMzz2afLLL___fazkemesA", \
                                       "timestamp": "1464627173923", \
                                       "v2messageType": "V2Message", \
                                       "streamId": "thread_id", \
                                       "message": "test string 2", \
                                       "attachments": [], \
                                       "fromUserId": 234567 \
                                      }]',
                               status=200,
                               content_type='text/json')
        # run query
        status_code, response = self.agent.read_datafeed('datafeed_id')
        # verify return
        assert status_code == 200

    def test_send_message(self):
        ''' test agent.send_message '''
        # register response
        httpretty.register_uri(httpretty.POST, self.__uri__ + "agent/v2/stream/thread_id/message/create",
                               body='{"id": "9zJTiQBL98ZEPAkvtjcweH___qr9auZ9dA", \
                                      "timestamp": "1464627173769", \
                                      "v2messageType": "V2Message", \
                                      "streamId": "thread_id", \
                                      "message": "test string", \
                                      "attachments": [], \
                                      "fromUserId": 123456 \
                                    }',
                               status=200,
                               content_type='text/json')
        # run test query
        status_code, response = self.agent.send_message('thread_id', 'TEXT', 'test string')
        response = json.loads(response)
        # verify return
        assert status_code == 200
        assert response['streamId'] == 'thread_id'
        assert response['message'] == 'test string'


if __name__ == '__main__':
    unittest.main()
