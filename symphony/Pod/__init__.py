#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        pod methods
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@nycresistor.com'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'


class Pod():
    from base import get_userid_by_email
    from base import get_user_id_by_user
    from base import adduser_to_stream
    from base import user_feature_update
    from base import search_user
    from connections import list_connections
    from connections import connection_status
    from connections import accept_connection
    from connections import create_connection

    def __init__(self, url, crt, key, session, keymngr):
        self.__url__ = url
        self.__crt__ = crt
        self.__key__ = key
        self.__session__ = session
        self.__keymngr__ = keymngr
