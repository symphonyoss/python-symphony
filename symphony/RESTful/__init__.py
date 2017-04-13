#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        RESTful methods
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@joyce.nyc'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'


class RESTful():
    from .base import GET_query
    from .base import POST_query

    def __init__(self, url, crt, key, session, keymngr):
        self.__url__ = url
        self.__crt__ = crt
        self.__key__ = key
        self.__session__ = session
        self.__keymngr__ = keymngr
