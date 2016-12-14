#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        Authentication Methods
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@nycresistor.com'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'

import json
import requests


class Auth():

    def __init__(self, keyurl, sessionurl, crt, key):
        self.__crt__ = crt
        self.__key__ = key
        self.__key_url__ = keyurl
        self.__session_url__ = sessionurl

    def get_session_token(self):
        ''' get session token '''
        # HTTP POST query to session authenticate API
        try:
            response = requests.post(self.__session_url__ + 'sessionauth/v1/authenticate',
                                     cert=(self.__crt__, self.__key__), verify=True)
        except requests.exceptions.RequestException as e:
            return e
        # load json response as list
        data = json.loads(response.text)
        if response.status_code == 200:
            # grab token from list
            session_token = data['token']
        else:
            session_token = 1
        # return the token
        return session_token

    def get_keymanager_token(self):
        ''' get keymanager token '''
        # HTTP POST query to keymanager authenticate API
        try:
            response = requests.post(self.__key_url__ + 'keyauth/v1/authenticate',
                                     cert=(self.__crt__, self.__key__), verify=True)
        except requests.exceptions.RequestException as e:
            return e
        # load json response as list
        data = json.loads(response.text)
        if response.status_code == 200:
            # grab token from list
            session_token = data['token']
        else:
            session_token = 1
        # return the token
        return session_token
