#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        Agent API Methods
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@nycresistor.com'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'


class Agent():
    from base import remove_control_characters
    from base import test_echo
    from base import create_datafeed
    from base import read_datafeed
    from base import send_message

    def __init__(self, url, crt, key, session, keymngr):
        self.__url__ = url
        self.__crt__ = crt
        self.__key__ = key
        self.__session__ = session
        self.__keymngr__ = keymngr
