#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        Unit Tests for Pod Group Methods
            - ib_group_list
            - ib_group_member_list
            - ib_group_member_add
            - ib_group_policy_list
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@joyce.nyc'
__copyright__ = 'Copyright 2017, Symphony Communication Services LLC'

import httpretty
import json
import unittest
import symphony


@httpretty.activate
class Pod_Group_tests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(Pod_Group_tests, self).__init__(*args, **kwargs)
        self.__uri__ = "http://fake.pod/"
        self.__session__ = "sessions"
        self.__keymngr__ = "keys"
        self.pod = symphony.Pod(self.__uri__, self.__session__, self.__keymngr__)

    def test_ib_group_list(self):
        ''' test pod.list_connections '''
        # register response
        httpretty.register_uri(httpretty.GET, self.__uri__ + "pod/v1/admin/group/list",
                               body='[{ \
                                       "id": "571db1f2e4b027c4f055a594", \
                                       "name": "Group 1", \
                                       "active": true, \
                                       "memberCount": 1, \
                                       "policies": [ \
                                         "571db2e4e4b012df6341f393" \
                                       ], \
                                       "createdDate": 1461563890135, \
                                       "modifiedDate": 1461563926812 \
                                      }, \
                                      { \
                                       "id": "571db20ae4b012df6341f391", \
                                       "name": "Group 2", \
                                       "active": true, \
                                       "memberCount": 1, \
                                       "policies": [ \
                                         "571db2e4e4b012df6341f393" \
                                       ], \
                                       "createdDate": 1461563914581, \
                                       "modifiedDate": 1461564112286 \
                                      }]',
                               status=200,
                               content_type='text/json')
        # run test query
        status_code, response = self.pod.ib_group_list()
        response = json.loads(response)
        # verify return
        assert status_code == 200
        assert response[0]['id'] == "571db1f2e4b027c4f055a594"
        assert response[1]['id'] == "571db20ae4b012df6341f391"

    def test_ib_group_member_list(self):
        ''' test pod.ib_group_member_list '''
        # register response
        httpretty.register_uri(httpretty.GET, self.__uri__ + "pod/v1/admin/group/87654/membership/list",
                               body='[ \
                                      123456 \
                                     ]',
                               status=200,
                               content_type='text/json')
        # run test query
        status_code, response = self.pod.ib_group_member_list('87654')
        # verify return
        response = json.loads(response)
        assert status_code == 200
        assert response[0] == 123456

    def test_ib_group_member_add(self):
        ''' test pod.ib_group_member_add '''
        # register response
        httpretty.register_uri(httpretty.POST, self.__uri__ + "pod/v1/admin/group/87654/membership/add",
                               body='{ \
                                      "overallResult": "SUCCESS", \
                                      "results": [ \
                                         "" \
                                      ] \
                                     }',
                               status=200,
                               content_type='text/json')
        # run query
        status_code, response = self.pod.ib_group_member_add('87654', ['123457', '567890'])
        # verify return
        response = json.loads(response)
        assert status_code == 200
        assert response['overallResult'] == "SUCCESS"

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
