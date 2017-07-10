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

    def user_feature_update(self, userid, payload):
        ''' update features by user id '''
        response, status_code = self.__pod__.User.post_v1_admin_user_uid_features_update(
            sessionToken=self.__session__,
            uid=userid,
            payload=payload
        ).result()
        return status_code, response

    def list_apps(self):
        ''' list apps '''
        response, status_code = self.__pod__.AppEntitlement.get_v1_admin_app_entitlement_list(
            sessionToken=self.__session__
        ).result()
        return status_code, response

    def create_stream_ni(self, user_ids):
        ''' create a stream in a non-inclusive manner '''
        req_hook = 'pod/v1/admin/im/create'
        req_args = json.dumps(user_ids)
        status_code, response = self.__rest__.POST_query(req_hook, req_args)
        return status_code, response

    def stream_members(self, stream_id):
        ''' get stream members '''
        req_hook = 'pod/v1/admin/stream/' + stream_id + '/membership/list'
        req_args = None
        status_code, response = self.__rest__.GET_query(req_hook, req_args)
        return status_code, response
