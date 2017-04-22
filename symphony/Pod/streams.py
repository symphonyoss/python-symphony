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
