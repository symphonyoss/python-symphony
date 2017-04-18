#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        Unit Tests for Pod Connections Methods
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
        httpretty.register_uri(httpretty.GET, self.__uri__ + "pod/v1/connection/list",
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
        status_code, response = self.pod.connection_status('123456')
        # verify return
        response = json.loads(response)
        assert status_code == 200
        assert response['status'] == "ACCEPTED"

    def test_accept_connection(self):
        ''' test pod.accept_connection '''
        # register response
        httpretty.register_uri(httpretty.POST, self.__uri__ + "pod/v1/connection/accept",
                               body='{ \
                                      "userId": 123456, \
                                      "status": "ACCEPTED", \
                                      "firstRequestedAt": 1471046357339, \
                                      "updatedAt": 1471046517684, \
                                      "requestCounter": 1 \
                                     }',
                               status=200,
                               content_type='text/json')
        # run query
        status_code, response = self.pod.accept_connection('123456')
        # verify return
        response = json.loads(response)
        assert status_code == 200
        assert response['userId'] == 123456
        assert response['status'] == "ACCEPTED"

    def test_create_connection(self):
        ''' test pod.create_connection '''
        # register response
        httpretty.register_uri(httpretty.POST, self.__uri__ + "pod/v1/connection/create",
                               body='{ \
                                      "userId": 123456, \
                                      "status": "PENDING_OUTGOING", \
                                      "firstRequestedAt": 1471018076255, \
                                      "updatedAt": 1471018076255, \
                                      "requestCounter": 1 \
                                     }',
                               status=200,
                               content_type='text/json')
        # run test query
        status_code, response = self.pod.create_connection('123456')
        response = json.loads(response)
        # verify return
        assert status_code == 200
        assert response['userId'] == 123456
        assert response['status'] == 'PENDING_OUTGOING'


if __name__ == '__main__':
    unittest.main()
