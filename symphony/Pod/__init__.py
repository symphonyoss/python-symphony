#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        pod methods
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@joyce.nyc'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'

import symphony


class Pod():
    # basic methods
    from .base import sessioninfo
    # user methods
    from .users import get_userid_by_email
    from .users import get_user_id_by_user
    from .users import user_feature_update
    from .users import search_user
    # streams methods
    from .streams import adduser_to_stream
    from .streams import create_stream
    from .streams import create_stream_ni
    from .streams import create_room
    from .streams import update_room
    from .streams import room_info
    from .streams import activate_stream
    from .streams import room_members
    # group methods
    from .groups import ib_group_list
    from .groups import ib_group_member_list
    from .groups import ib_group_member_add
    from .groups import ib_group_policy_list
    # connection methods
    from .connections import list_connections
    from .connections import connection_status
    from .connections import accept_connection
    from .connections import create_connection

    def __init__(self, url, session, keymngr):
        self.__url__ = url
        self.__session__ = session
        self.__keymngr__ = keymngr
        self.__rest__ = symphony.RESTful(self.__url__, self.__session__, self.__keymngr__)
