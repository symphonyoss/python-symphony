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


class Agent_tests(unittest.TestCase):

    @httpretty.activate
    def test_test_echo(self):
        ''' test get_user_id_by_email '''
        # register response
        httpretty.register_uri(httpretty.GET, "http://fake.pod/agent/v1/util/echo",
                               body='{"message": "test string"}',
                               status=200,
                               content_type='text/json')
        # dummy authenticate
        symphony_pod_uri = 'http://fake.pod/'
        session_token = 'sessions'
        keymngr_token = 'keys'
        agent = symphony.Agent(symphony_pod_uri, session_token, keymngr_token)
        # run test query
        status_code, response = agent.test_echo('test string')
        response = json.loads(response)
        # verify return
        assert status_code == 200
        # assert response['message'] == "test string"

    @httpretty.activate
    def test_create_datafeed(self):
        ''' test user_feature_update '''
        # register response
        httpretty.register_uri(httpretty.POST, "http://fake.pod/agent/v1/datafeed/create",
                               body='{ "id": 78910 }',
                               status=200,
                               content_type='text/json')
        # dummy authenticate
        symphony_pod_uri = 'http://fake.pod/'
        session_token = 'sessions'
        keymngr_token = 'keys'
        agent = symphony.Agent(symphony_pod_uri, session_token, keymngr_token)
        # run test query
        status_code, response = agent.create_datafeed()
        # verify return
        assert status_code == 200
        assert response == 78910

    @httpretty.activate
    def test_send_message(self):
        ''' test get_user_id_by_email '''
        # register response
        httpretty.register_uri(httpretty.POST, "http://fake.pod/agent/v2/stream/thread_id/message/create",
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
        # dummy authenticate
        symphony_pod_uri = 'http://fake.pod/'
        session_token = 'sessions'
        keymngr_token = 'keys'
        agent = symphony.Agent(symphony_pod_uri, session_token, keymngr_token)
        # run test query
        status_code, response = agent.send_message('thread_id', 'TEXT', 'test string')
        response = json.loads(response)
        # verify return
        assert status_code == 200
        assert response['streamId'] == 'test string'


if __name__ == '__main__':
    unittest.main()
