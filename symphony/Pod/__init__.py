#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        pod methods
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@nycresistor.com'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'

import symphony


class Pod():
    from .base import sessioninfo
    from .users import get_userid_by_email
    from .users import get_user_id_by_user
    from .users import adduser_to_stream
    from .users import user_feature_update
    from .users import search_user
    from .connections import list_connections
    from .connections import connection_status
    from .connections import accept_connection
    from .connections import create_connection

    def __init__(self, url, crt, key, session, keymngr):
        self.__url__ = url
        self.__crt__ = crt
        self.__key__ = key
        self.__session__ = session
        self.__keymngr__ = keymngr
        self.__rest__ = symphony.RESTful(self.__url__, self.__crt__, self.__key__, self.__session__, self.__keymngr__)
