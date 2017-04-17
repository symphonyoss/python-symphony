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

    def __init__(self):
        self.__uri__ = "http://fake.pod/"

    @httpretty.activate
    def test_get_user_id_by_email(self):
        ''' test get_user_id_by_email '''
        # register response
        httpretty.register_uri(httpretty.GET, self.__uri__ + "/pod/v1/user",
                               body='{"userId": 123456 }',
                               status=500,
                               content_type='text/json')
        # dummy authenticate
        symphony_pod_uri = 'http://fake.pod/'
        session_token = 'sessions'
        keymngr_token = 'keys'
        pod = symphony.Pod(symphony_pod_uri, session_token, keymngr_token)
        # run test query
        response = pod.get_userid_by_email('test@fake.pod')
        # verify return
        assert response.text == "123456"


if __name__ == '__main__':
    unittest.main()
