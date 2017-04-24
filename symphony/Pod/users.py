#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        pod endpoint Users methods
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@joyce.nyc'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'

import json


class Users(object):

    def __init__(self, *args, **kwargs):
        super(Users, self).__init__(*args, **kwargs)

    def get_userid_by_email(self, email):
        ''' get userid by email '''
        req_hook = 'pod/v1/user'
        req_args = '?email=' + email
        status_code, response = self.__rest__.GET_query(req_hook, req_args)
        return status_code, response

    def get_user_id_by_user(self, username):
        ''' get user id by username '''
        req_hook = 'pod/v1/user/name/' + username + '/get'
        req_args = None
        status_code, response = self.__rest__.GET_query(req_hook, req_args)
        return status_code, response

    def user_presence(self, userid):
        ''' check on presence of a user '''
        req_hook = 'pod/v2/user/' + str(userid) + '/presence'
        req_args = None
        status_code, response = self.__rest__.GET_query(req_hook, req_args)
        return status_code, response

    def list_features(self):
        ''' list features the pod supports '''
        req_hook = 'pod/v1/admin/system/features/list'
        req_args = None
        status_code, response = self.__rest__.GET_query(req_hook, req_args)
        return status_code, response

    def user_feature_update(self, userid, req_args):
        ''' update features by user id '''
        req_hook = 'pod/v1/admin/user/' + str(userid) + '/features/update'
        status_code, response = self.__rest__.POST_query(req_hook, req_args)
        return status_code, response

    def search_user(self, search_str, search_filter, local):
        ''' add a user to a stream '''
        req_hook = 'pod/v1/user/search?local=' + local
        req_args = {
            "query": search_str,
            "filters": search_filter
        }
        req_args = json.dumps(req_args)
        status_code, response = self.__rest__.POST_query(req_hook, req_args)
        return status_code, response

    def list_apps(self):
        ''' list apps '''
        req_hook = 'pod/v1/admin/app/entitlement/list'
        req_args = None
        status_code, response = self.__rest__.GET_query(req_hook, req_args)
        return status_code, response
