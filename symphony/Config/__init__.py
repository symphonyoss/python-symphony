#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        Module configuration methods
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@joyce.nyc'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'

import configparser
import logging
import sys
import symphony


class Config:

    def __init__(self, config):
        ''' command line argument parsing '''
        self.__config__ = config

    def connect(self):
        ''' instantiate objects / parse config file '''
        # open config file for parsing
        try:
            settings = configparser.ConfigParser()
            settings._interpolation = configparser.ExtendedInterpolation()
        except Exception as err:
            logging.error("Failed to instantiate config parser exception: %s" % err)
        try:
            settings.read(self.__config__)
        except Exception as err:
            logging.error("Failed to read config file exception: %s" % err)
            sys.exit(2)

        # Connect to Symphony
        symphony_p12 = settings.get('symphony', 'symphony_p12')
        symphony_pwd = settings.get('symphony', 'symphony_pwd')
        symphony_pod_uri = settings.get('symphony', 'symphony_pod_uri')
        symphony_keymanager_uri = settings.get('symphony', 'symphony_keymanager_uri')
        symphony_agent_uri = settings.get('symphony', 'symphony_agent_uri')
        symphony_sessionauth_uri = settings.get('symphony', 'symphony_sessionauth_uri')
        symphony_sid = settings.get('symphony', 'symphony_sid')
        crypt = symphony.Crypt(symphony_p12, symphony_pwd)
        symphony_crt, symphony_key = crypt.p12parse()

        try:
            # instantiate auth methods
            auth = symphony.Auth(symphony_sessionauth_uri, symphony_keymanager_uri, symphony_crt, symphony_key)
            # get session token
            session_token = auth.get_session_token()
            logging.info("AUTH ( session token ): %s" % session_token)
            # get keymanager token
            keymngr_token = auth.get_keymanager_token()
            logging.info("AUTH ( key manager token ): %s" % keymngr_token)
            # instantiate agent methods
            agent = symphony.Agent(symphony_agent_uri, session_token, keymngr_token)
            # instantiate pod methods
            pod = symphony.Pod(symphony_pod_uri, session_token, keymngr_token)

            logging.info("INSTANTIATION ( all objects successful)")
        except Exception as err:
            logging.error("Failed to authenticate and initialize: %s" % err)
            return 'you', 'have', 'failed'
        # return references and such
        return agent, pod, symphony_sid
