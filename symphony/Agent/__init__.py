#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        Agent API Methods
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@joyce.nyc'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'


import symphonybinding

from .base import Base


class Agent(Base):

    def __init__(self, url, session, keymngr, crt, key):
        self.__url__ = url
        self.__session__ = session
        self.__keymngr__ = keymngr
        self.__crt__ = crt
        self.__key__ = key
        try:
            CG = symphonybinding.SymCodegen()
            self.__agent__, self.__agentdepr__ = CG.agent_cg(self.__url__)
        except Exception as err:
            print err
