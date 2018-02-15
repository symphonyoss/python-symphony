#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        Pod API Methods
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@joyce.nyc'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'


import symphonybinding
import logging

from .users import Users
from .streams import Streams
from .groups import Groups
from .connections import Connections
from .admin import Admin
from .base import Base


class Pod(Base, Users, Streams, Groups, Connections, Admin):

    def __init__(self, url, session, keymngr, logger=None):
        self.__url__ = url
        self.__session__ = session
        self.__keymngr__ = keymngr
        self.logger = logger or logging.getLogger(__name__)
        try:
            CG = symphonybinding.SymCodegen()
            self.__pod__ = CG.pod_cg(self.__url__)
        except Exception as err:
            self.logger.error(err)
            raise

    def get_session_token(self):
        self.logger.warn('user exported session token: %s' % self.__session__)
        return self.__session__
