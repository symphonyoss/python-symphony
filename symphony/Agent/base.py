#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        Agent API Methods
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@joyce.nyc'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'

import ast
import json
import unicodedata


class Base(object):

    def __init__(self, *args, **kwargs):
        super(Base, self).__init__(*args, **kwargs)

    def remove_control_characters(self, s):
        return "".join(ch for ch in s if unicodedata.category(ch)[0] != "C")

    def test_echo(self, test_string):
        ''' echo test '''
        req_hook = 'agent/v1/util/echo'
        # test message
        req_args = '{ "message": "'"%s"'" }' % test_string
        # receive HTTP response code and response text
        status_code, response = self.__rest__.PKCS_POST_query(req_hook, req_args)
        # return the token
        return status_code, response

    def create_datafeed(self):
        ''' create datafeed '''
        req_hook = 'agent/v1/datafeed/create'
        req_args = None
        status_code, response = self.__rest__.PKCS_POST_query(req_hook, req_args)
        # load json response as list
        datafeed = json.loads(response)
        # return the token
        return status_code, datafeed['id']

    def read_datafeed(self, streamid):
        ''' get datafeed '''
        req_hook = 'agent/v1/datafeed/' + str(streamid) + '/read'
        req_args = None
        status_code, response = self.__rest__.PKCS_GET_query(req_hook, req_args)
        response = ast.literal_eval(response)
        return status_code, response

    def send_message(self, threadid, msgFormat, message):
        ''' send message to threadid/stream '''
        req_hook = 'agent/v2/stream/' + threadid + '/message/create'
        req_args = '{ "format": "%s", "message": "'"%s"'" }' % (msgFormat, message)
        status_code, response = self.__rest__.PKCS_POST_query(req_hook, req_args)
        return status_code, response
