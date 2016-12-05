#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        pod methods
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@nycresistor.com'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'

import json
import requests


class Pod():
    from pod import pod
    from connections import connections   
   
    def __init__(self, url, crt, key, session, keymngr):
        self.__url__ = url
        self.__crt__ = crt
        self.__key__ = key
        self.__session__ = session
        self.__keymngr__ = keymngr

