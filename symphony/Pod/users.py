#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        pod endpoint Users methods
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@joyce.nyc'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'


class Users(object):

    def __init__(self, *args, **kwargs):
        super(Users, self).__init__(*args, **kwargs)

    def get_userid_by_email(self, email):
        ''' get userid by email '''
        response, status_code = self.__pod__.Users.get_v2_user(
            sessionToken=self.__session__,
            email=email
        ).result()
        return status_code, response

    def get_user_id_by_user(self, username):
        ''' get user id by username '''
        response, status_code = self.__pod__.Users.get_v2_user(
            sessionToken=self.__session__,
            username=username
        ).result()
        return status_code, response

    def user_presence(self, userid):
        ''' check on presence of a user '''
        response, status_code = self.__pod__.Presence.get_v2_user_uid_presence(
            sessionToken=self.__session__,
            uid=userid
        ).result()
        return status_code, response

    def search_user(self, search_str, search_filter, local):
        ''' add a user to a stream '''
        response, status_code = self.__pod__.Users.post_v1_user_search(
            sessionToken=self.__session__,
            searchRequest={'query': search_str,
                           'filters': search_filter}
        ).result()
        return status_code, response
