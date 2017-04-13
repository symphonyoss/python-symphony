#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        Agent API Methods
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@nycresistor.com'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'

import ast
import json
import unicodedata


def remove_control_characters(self, s):
    return "".join(ch for ch in s if unicodedata.category(ch)[0] != "C")


def test_echo(self, test_string):
    ''' echo test '''
    # REST API method endpoint
    req_hook = 'agent/v1/util/echo'
    # test message
    req_args = '{ "message": "'"%s"'" }' % test_string
    # receive HTTP response code and response text
    status_code, response = self.REST.POST_query(req_hook, req_args)
    # return the token
    return status_code


def create_datafeed(self):
    ''' create datafeed '''
    # REST API method endpoint
    req_hook = 'agent/v1/datafeed/create'
    req_args = None
    status_code, response = self.REST.POST_query(req_hook, req_args)
    # load json response as list
    datafeed = json.loads(response)
    # return the token
    return datafeed['id']


def read_datafeed(self, streamid):
    ''' get datafeed '''
    # REST API method endpoint
    req_hook = 'agent/v1/datafeed/' + str(streamid) + '/read'
    req_args = None
    status_code, response = self.REST.GET_query(req_hook, req_args)
    response = ast.literal_eval(response)
    return response, status_code


def send_message(self, threadid, msgFormat, message):
    ''' send message to threadid/stream '''
    # REST API method endpoint
    req_hook = 'agent/v2/stream/' + threadid + '/message/create'
    req_args = '{ "format": "%s", "message": "'"%s"'" }' % (msgFormat, message)
    status_code, response = self.REST.POST_query(req_hook, req_args)
    return response
