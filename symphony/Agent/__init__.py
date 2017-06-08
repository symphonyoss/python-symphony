#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        Agent API Methods
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@joyce.nyc'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'


import symphony

from .base import Base


class Agent(Base):

    def __init__(self, url, session, keymngr, crt, key):
        self.__url__ = url
        self.__session__ = session
        self.__keymngr__ = keymngr
        self.__crt__ = crt
        self.__key__ = key
        self.__rest__ = symphony.RESTful(self.__url__, self.__session__, self.__keymngr__, self.__crt__, self.__key__)
