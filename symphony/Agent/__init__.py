#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        Agent API Methods
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@joyce.nyc'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'

import logging
import symphonybinding

from .base import Base


class Agent(Base):

    def __init__(self, url, session, keymngr, logger=None):
        self.__url__ = url
        self.__session__ = session
        self.__keymngr__ = keymngr
        self.logger = logger or logging.getLogger(__name__)
        try:
            CG = symphonybinding.SymCodegen()
            self.__agent__ = CG.agent_cg(self.__url__)
        except Exception as err:
            self.logger.error(err)

    def get_keymanager_token(self):
        self.logger.warn('user exported keymanager token: %s' % self.__keymngr__)
        return self.__keymngr__
