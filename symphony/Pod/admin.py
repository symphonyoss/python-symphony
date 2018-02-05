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
        self.logger.debug('%s: %s' % (status_code, response))
        return status_code, response

    def user_feature_update(self, userid, payload):
        ''' update features by user id '''
        response, status_code = self.__pod__.User.post_v1_admin_user_uid_features_update(
            sessionToken=self.__session__,
            uid=userid,
            payload=payload
        ).result()
        self.logger.debug('%s: %s' % (status_code, response))
        return status_code, response

    def get_user_avatar(self, userid):
        ''' get avatar by user id '''
        response, status_code = self.__pod__.User.get_v1_admin_user_uid_avatar(
            sessionToken=self.__session,
            uid=userid
        ).result()
        self.logger.debug('%s: %s' % (status_code, response))
        return status_code, response

    def user_avatar_update(self, userid, payload):
        ''' updated avatar by userid '''
        response, status_code = self.__pod__.User.post_v1_admin_user_uid_avatar_update(
            sessionToken=self.__session,
            uid=userid,
            payload=payload
        ).result()
        self.logger.debug('%s: %s' % (status_code, response))
        return status_code, response

    def list_apps(self):
        ''' list apps '''
        response, status_code = self.__pod__.AppEntitlement.get_v1_admin_app_entitlement_list(
            sessionToken=self.__session__
        ).result()
        self.logger.debug('%s: %s' % (status_code, response))
        return status_code, response

    def stream_members(self, stream_id):
        ''' get stream members '''
        response, status_code = self.__pod__.Streams.get_v1_admin_stream_id_membership_list(
            sessionToken=self.__session__,
            id=stream_id
        ).result()
        self.logger.debug('%s: %s' % (status_code, response))
        return status_code, response
