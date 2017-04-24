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

    def list_connections(self):
        ''' list connections '''
        req_hook = 'pod/v1/connection/list?status=all'
        req_args = None
        status_code, response = self.__rest__.GET_query(req_hook, req_args)
        return status_code, response

    def connection_status(self, userid):
        ''' get connection status '''
        req_hook = 'pod/v1/connection/' + userid + '/info'
        req_args = None
        status_code, response = self.__rest__.GET_query(req_hook, req_args)
        return status_code, response

    def accept_connection(self, userid):
        ''' accept connection request '''
        req_hook = 'pod/v1/connection/accept'
        req_args = '{ "userId": %s }' % userid
        status_code, response = self.__rest__.POST_query(req_hook, req_args)
        return status_code, response

    def create_connection(self, userid):
        ''' create connection '''
        req_hook = 'pod/v1/connection/create'
        req_args = '{ "userId": %s }' % userid
        status_code, response = self.__rest__.POST_query(req_hook, req_args)
        return status_code, response
