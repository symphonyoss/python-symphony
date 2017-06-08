#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        RESTful methods
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@joyce.nyc'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'

from .nopkcs import NOPKCS
from .pkcs import PKCS


class RESTful(NOPKCS, PKCS):

    def __init__(self, url, session, keymngr, crt=None, key=None):
        self.__url__ = url
        self.__session__ = session
        self.__keymngr__ = keymngr
        self.__crt__ = crt
        self.__key__ = key

    def bool2str(self, boolval):
        if boolval:
            return 'true'
        else:
            return 'false'
