#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        Unit Tests for Agent Methods
            - list_connections
            - connection_status
            - accept_connection
            - create_connection
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@joyce.nyc'
__copyright__ = 'Copyright 2017, Symphony Communication Services LLC'

import httpretty
import json
import unittest
import symphony


@httpretty.activate
class Pod_Connections_tests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(Pod_Connections_tests, self).__init__(*args, **kwargs)
        self.__uri__ = "http://fake.pod/"
        self.__session__ = "sessions"
        self.__keymngr__ = "keys"
        self.pod = symphony.Pod(self.__uri__, self.__session__, self.__keymngr__)

    def test_list_connections(self):
        ''' test pod.list_connections '''
        # register response
        httpretty.register_uri(httpretty.GET, self.__uri__ + "pod/v1/connection/list?status=all",
                               body='[{ \
                                       "userId": 7078106126503, \
                                       "status": "PENDING_OUTGOING", \
                                       "updatedAt": 1471018076255 \
                                      }, \
                                      { \
                                       "userId": 7078106103809, \
                                       "status": "PENDING_INCOMING", \
                                       "updatedAt": 1467562406219 \
                                      } \
                                     ]',
                               status=200,
                               content_type='text/json')
        # run test query
        status_code, response = self.pod.list_connections()
        response = json.loads(response)
        # verify return
        assert status_code == 200
        assert response[0]['userId'] == 7078106126503

    def test_connection_status(self):
        ''' test pod.connection_status '''
        # register response
        httpretty.register_uri(httpretty.GET, self.__uri__ + "pod/v1/connection/123456/info",
                               body='{ \
                                      "userId": 123456, \
                                      "status": "ACCEPTED" \
                                     }',
                               status=200,
                               content_type='text/json')
        # run test query
        status_code, response = self.pod.connection_status()
        # verify return
        response = json.loads(response)
        assert status_code == 200
        assert response['status'] == "ACCEPTED"

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
