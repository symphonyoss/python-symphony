#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        Authentication Methods
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@joyce.nyc'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'

import json
import requests
import logging


class Auth():

    def __init__(self, keyurl, sessionurl, crt, key, logger=None):
        self.__crt__ = crt
        self.__key__ = key
        self.__key_url__ = keyurl
        self.__session_url__ = sessionurl
        self.logger = logger or logging.getLogger(__name__)

    def get_session_token(self):
        ''' get session token '''
        # HTTP POST query to session authenticate API
        try:
            response = requests.post(self.__session_url__ + 'sessionauth/v1/authenticate',
                                     cert=(self.__crt__, self.__key__), verify=True)
        except requests.exceptions.RequestException as err:
            self.logger.error(err)
            raise
        if response.status_code == 200:
            # load json response as list
            data = json.loads(response.text)
            self.logger.debug(data)
            # grab token from list
            session_token = data['token']
        else:
            raise Exception('BAD HTTP STATUS: %s' % str(response.status_code))
        # return the token
        self.logger.debug(session_token)
        return session_token

    def get_keymanager_token(self):
        ''' get keymanager token '''
        # HTTP POST query to keymanager authenticate API
        try:
            response = requests.post(self.__key_url__ + 'keyauth/v1/authenticate',
                                     cert=(self.__crt__, self.__key__), verify=True)
        except requests.exceptions.RequestException as err:
            self.logger.error(err)
            raise
        if response.status_code == 200:
            # load json response as list
            data = json.loads(response.text)
            self.logger.debug(data)
            # grab token from list
            session_token = data['token']
        else:
            raise Exception('BAD HTTP STATUS: %s' % str(response.status_code))
        # return the token
        self.logger.debug(session_token)
        return session_token
