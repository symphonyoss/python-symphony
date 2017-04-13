#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        connections methods
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@nycresistor.com'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'

import json
import symphony


def list_connections(self):
    ''' list connections '''
    # instantiate RESTful class()
    REST = symphony.RESTful()
    # REST API method endpoint
    req_hook = 'pod/v1/connection/list?status=all'
    req_args = None
    status_code, response = REST.GET_query(req_hook, req_args)
    connections = json.loads(response)
    return connections


def connection_status(self, userid):
    ''' get connection status '''
    # instantiate RESTful class()
    REST = symphony.RESTful()
    # REST API method endpoint
    req_hook = 'pod/v1/connection/' + userid + '/info'
    req_args = None
    status_code, response = REST.GET_query(req_hook, req_args)
    connection_status = json.loads(response)
    return connection_status


def accept_connection(self, userid):
    ''' accept connection request '''
    # instantiate RESTful class()
    REST = symphony.RESTful()
    # REST API method endpoint
    req_hook = 'pod/v1/connection/accept'
    req_args = '{ "userId": %s }' % userid
    status_code, response = REST.POST_query(req_hook, req_args)
    return status_code, response


def create_connection(self, userid):
    ''' create connection '''
    # instantiate RESTful class()
    REST = symphony.RESTful()
    # REST API method endpoint
    req_hook = 'pod/v1/connection/create'
    req_args = '{ "userId": %s }' % userid
    status_code, response = REST.POST_query(req_hook, req_args)
    return status_code, response
