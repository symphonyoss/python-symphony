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
    def test_get_user_id_by_email(self):
        ''' test get_user_id_by_email '''
        # register response
        httpretty.register_uri(httpretty.GET, "http://fake.pod/",
                               body="{userId: '123456'}")
        # dummy authenticate
        conn = symphony.Config('dummy-test.cfg')
        agent, pod, symphony_sid = conn.dummy_connect()

        # run test query
        status_code, response = pod.get_userid_by_email('test@email.com')
        # verify return
        assert response.text == "{userId: '123456'}"


if __name__ == '__main__':
    unittest.main()
