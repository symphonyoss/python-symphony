#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        Unit Tests for Pod Methods related to Users
            - get_userid_by_email
            - get_user_id_by_user
            - adduser_to_stream
            - user_feature_update
            - search_user
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@joyce.nyc'
__copyright__ = 'Copyright 2017, Symphony Communication Services LLC'

import httpretty
import unittest
import symphony


class Pod_Users_test(unittest.TestCase):

    @httpretty.activate
    def test_get_userid_by_email(self):
        ''' test get_user_id_by_email '''
        # register response
        httpretty.register_uri(httpretty.GET, "http://fake.pod/pod/v1/user",
                               body='{"id": 123456, "emailAddress": "test@fake.pod" }',
                               status=200,
                               content_type='text/json')
        # dummy authenticate
        symphony_pod_uri = 'http://fake.pod/'
        session_token = 'sessions'
        keymngr_token = 'keys'
        pod = symphony.Pod(symphony_pod_uri, session_token, keymngr_token)
        # run test query
        response = pod.get_userid_by_email('test@fake.pod')
        # verify return
        assert response['id'] == 123456
        assert response['emailAddress'] == "test@fake.pod"

    @httpretty.activate
    def test_get_user_id_by_user(self):
        ''' test get_user_id_by_user '''
        # register response
        httpretty.register_uri(httpretty.GET, "http://fake.pod/pod/v1/user/name/testuser/get",
                               body='{"id": 123456, "emailAddress": "test@fake.pod" }',
                               status=200,
                               content_type='text/json')
        # dummy authenticate
        symphony_pod_uri = 'http://fake.pod/'
        session_token = 'sessions'
        keymngr_token = 'keys'
        pod = symphony.Pod(symphony_pod_uri, session_token, keymngr_token)
        # run test query
        response = pod.get_user_id_by_user('testuser')
        # verify return
        assert response['id'] == 123456
        assert response['emailAddress'] == "test@fake.pod"

    @httpretty.activate
    def test_adduser_to_stream(self):
        ''' test adduser_to_stream '''
        # register response
        httpretty.register_uri(httpretty.POST, "http://fake.pod/pod/v1/room/stream_id/membership/add",
                               body='{ "format": "TEXT", "message": "Member added" }',
                               status=200,
                               content_type='text/json')
        # dummy authenticate
        symphony_pod_uri = 'http://fake.pod/'
        session_token = 'sessions'
        keymngr_token = 'keys'
        pod = symphony.Pod(symphony_pod_uri, session_token, keymngr_token)
        # run test query
        status_code, response = pod.adduser_to_stream('stream_id', '123456')
        # verify return
        assert status_code == 200

    @httpretty.activate
    def test_user_feature_update(self):
        ''' test user_feature_update '''
        # register response
        httpretty.register_uri(httpretty.POST, "http://fake.pod/pod/v1/admin/user/123456/features/update",
                               body='{ "format": "TEXT", "message": "OK" }',
                               status=200,
                               content_type='text/json')
        # dummy authenticate
        symphony_pod_uri = 'http://fake.pod/'
        session_token = 'sessions'
        keymngr_token = 'keys'
        pod = symphony.Pod(symphony_pod_uri, session_token, keymngr_token)
        # run test query
        test_feature_query = '[{"entitlment": "isExternalRoomEnabled", "enabled": true },'\
                             '{"entitlment": "isExternalIMEnabled", "enabled": true }]'
        status_code, response = pod.user_feature_update('123456', test_feature_query)
        # verify return
        assert status_code == 200


if __name__ == '__main__':
    unittest.main()
