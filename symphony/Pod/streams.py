#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        pod endpoint streams methods
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@joyce.nyc'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'

import json


def adduser_to_stream(self, streamid, userid):
    ''' add a user to a stream '''
    req_hook = 'pod/v1/room/' + streamid + '/membership/add'
    req_args = '{ "id": %s }' % userid
    status_code, response = self.__rest__.POST_query(req_hook, req_args)
    return status_code, response


def create_stream(self):
    ''' create a stream '''
    req_hook = 'pod/v1/im/create'
    req_args = None
    status_code, response = self.__rest__.POST_query(req_hook, req_args)
    return status_code, response


def create_stream_ni(self, userids):
    ''' create a stream in a non-inclusive manner '''
    req_hook = 'pod/v1/admin/im/create'
    req_args = json.dumps(userids)
    status_code, response = self.__rest__.POST_query(req_hook, req_args)
    return status_code, response


def create_room(self, room_definition):
    ''' create's a room '''
    req_hook = 'pod/v2/room/create'
    req_args = json.dumps(room_definition)
    status_code, response = self.__rest__.POST_query(req_hook, req_args)
    return status_code, response


def update_room(self, stream_id, room_definition):
    ''' update a room definition '''
    req_hook = 'pod/v2/room/' + stream_id + '/update'
    req_args = json.dumps(room_definition)
    status_code, response = self.__rest__.POST_query(req_hook, req_args)
    return status_code, response
