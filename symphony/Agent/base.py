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
import requests
import unicodedata


def remove_control_characters(self, s):
    return "".join(ch for ch in s if unicodedata.category(ch)[0] != "C")


def test_echo(self, test_string):
    ''' echo test '''

    headers = {'Content-Type': 'application/json',
               'sessionToken': self.__session__,
               'keyManagerToken': self.__keymngr__}

    data = '{ "message": "'"%s"'" }' % test_string

    # HTTP POST query to keymanager authenticate API
    try:
        response = requests.post(self.__url__ + 'agent/v1/util/echo',
                                 headers=headers,
                                 data=data,
                                 cert=(self.__crt__, self.__key__),
                                 verify=True)
    except requests.exceptions.RequestException as e:
        print e
        return None
    # load json response as list
    status_code = response.text
    # return the token
    return status_code


def create_datafeed(self):
    ''' create datafeed '''
    # https://your-pod.symphony.com/:8444/agent/v1/datafeed/create
    headers = {'Content-Type': 'application/json',
               'sessionToken': self.__session__,
               'keyManagerToken': self.__keymngr__}

    # HTTP POST query to keymanager authenticate API
    try:
        response = requests.post(self.__url__ + 'agent/v1/datafeed/create',
                                 headers=headers,
                                 cert=(self.__crt__, self.__key__),
                                 verify=True)
    except requests.exceptions.RequestException as e:
        print e
        return None
    # load json response as list
    datafeed = json.loads(response.text)
    # return the token
    return datafeed['id']


def read_datafeed(self, streamid):
    ''' get datafeed '''
    headers = {'Content-Type': 'application/json',
               'sessionToken': self.__session__,
               'keyManagerToken': self.__keymngr__}

    # HTTP POST query to keymanager authenticate API
    try:
        response = requests.get(self.__url__ + 'agent/v2/datafeed/' + str(streamid) + '/read',
                                headers=headers,
                                cert=(self.__crt__, self.__key__),
                                verify=True)
    except requests.exceptions.RequestException as e:
        print e
        return None
    # load json response as list
    datafeed = response.text
    datastat = response.status_code
    if datastat == 200:
        datafeed = ast.literal_eval(datafeed)
    # return the token
    return datafeed, datastat


def send_message(self, threadid, msgFormat, message):
    ''' send message to threadid/stream '''
    message = self.remove_control_characters(message)
    headers = {'content-type': 'application/json',
               'sessionToken': self.__session__,
               'keyManagerToken': self.__keymngr__}
    data = '{ "format": "%s", "message": "'"%s"'" }' % (msgFormat, message)
    # HTTP POST query to keymanager authenticate API
    try:
        response = requests.post(self.__url__ + 'agent/v2/stream/' + threadid + '/message/create',
                                 headers=headers,
                                 data=data,
                                 cert=(self.__crt__, self.__key__),
                                 verify=True)
    except requests.exceptions.RequestException as e:
        print e
        return None
    # load json response as list
    string = response.text
    # return the token
    return string
