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
        response = self.__agent__.Util.post_v1_util_echo(sessionToken=self.__session__,
                                                         keyManagerToken=self.__keymngr__,
                                                         echoInput={"message": test_string}
                                                         ).result()
        return response

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
        # using deprecated v3 message create because of bug in codegen of v4 ( multipart/form-data )
        response = self.__agentdepr__.Messages.post_v3_stream_sid_message_create(sessionToken=self.__session__,
                                                                                 keyManagerToken=self.__keymngr__,
                                                                                 sid=threadid,
                                                                                 message={"format": msgFormat,
                                                                                 "message": message}
                                                                                 ).result()
        return response
