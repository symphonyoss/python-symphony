#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        pod endpoint Admin methods
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@joyce.nyc'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'


class Admin(object):

    def __init__(self, *args, **kwargs):
        super(Admin, self).__init__(*args, **kwargs)

    def list_features(self):
        ''' list features the pod supports '''
        response, status_code = self.__pod__.System.get_v1_admin_system_features_list(
            sessionToken=self.__session__
        ).result()
        return status_code, response

    def user_feature_update(self, userid, req_args):
        ''' update features by user id '''
        req_hook = 'pod/v1/admin/user/' + str(userid) + '/features/update'
        status_code, response = self.__rest__.POST_query(req_hook, req_args)
        return status_code, response

    def list_apps(self):
        ''' list apps '''
        req_hook = 'pod/v1/admin/app/entitlement/list'
        req_args = None
        status_code, response = self.__rest__.GET_query(req_hook, req_args)
        return status_code, response
