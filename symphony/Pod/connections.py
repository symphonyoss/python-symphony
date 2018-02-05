#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        connections methods
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@joyce.nyc'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'


class Connections(object):

    def __init__(self, *args, **kwargs):
        super(Connections, self).__init__(*args, **kwargs)

    def sessioninfo(self):
        ''' session info '''
        response, status_code = self.__pod__.Session.get_v2_sessioninfo(
            sessionToken=self.__session__
        ).result()
        self.logger.debug('%s: %s' % (status_code, response))
        return status_code, response

    def list_connections(self, status=None):
        ''' list connections '''
        if status is None:
            status = 'ALL'
        response, status_code = self.__pod__.Connection.get_v1_connection_list(
            sessionToken=self.__session__,
            status=status
        ).result()
        self.logger.debug('%s: %s' % (status_code, response))
        return status_code, response

    def connection_status(self, userid):
        ''' get connection status '''
        response, status_code = self.__pod__.Connection.get_v1_connection_user_userId_info(
            sessionToken=self.__session__,
            userId=userid
        ).result()
        self.logger.debug('%s: %s' % (status_code, response))
        return status_code, response

    def accept_connection(self, userid):
        ''' accept connection request '''
        req_hook = 'pod/v1/connection/accept'
        req_args = '{ "userId": %s }' % userid
        status_code, response = self.__rest__.POST_query(req_hook, req_args)
        self.logger.debug('%s: %s' % (status_code, response))
        return status_code, response

    def create_connection(self, userid):
        ''' create connection '''
        req_hook = 'pod/v1/connection/create'
        req_args = '{ "userId": %s }' % userid
        status_code, response = self.__rest__.POST_query(req_hook, req_args)
        self.logger.debug('%s: %s' % (status_code, response))
        return status_code, response
