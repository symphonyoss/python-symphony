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
import requests


def list_connections(self):
    ''' list connections '''
    headers = {'content-type': 'application/json',
               'sessionToken': self.__session__}

    try:
        response = requests.get(self.__url__ + 'pod/v1/connection/list?status=all',
                                headers=headers,
                                cert=(self.__crt__, self.__key__),
                                verify=True)
    except requests.exceptions.RequestException as e:
        print e
        return None
    # load json response as list
    connections = json.loads(response.text)
    # return the token
    return connections


def connection_status(self, userid):
    ''' get connection status '''
    headers = {'content-type': 'application/json',
               'sessionToken': self.__session__}

    try:
        response = requests.get(self.__url__ + 'pod/v1/connection/' + userid + '/info',
                                headers=headers,
                                cert=(self.__crt__, self.__key__),
                                verify=True)
    except requests.exceptions.RequestException as e:
        print e
        return None
    # load json response as list
    connection_status = json.loads(response.text)
    # return the token
    return connection_status


def accept_connection(self, userid):
    ''' accept connection request '''
    headers = {'Content-Type': 'application/json',
               'sessionToken': self.__session__}

    data = '{ "userId": %s }' % userid

    # HTTP POST query to keymanager authenticate API
    try:
        response = requests.post(self.__url__ + 'pod/v1/connection/accept',
                                 headers=headers,
                                 data=data,
                                 cert=(self.__crt__, self.__key__),
                                 verify=True)
    except requests.exceptions.RequestException as e:
        print e
        return None
    # return the token
    return response.status_code, response.text


def create_connection(self, userid):
    ''' create connection '''
    headers = {'Content-Type': 'application/json',
               'sessionToken': self.__session__}

    data = '{ "userId": %s }' % userid

    # HTTP POST query to keymanager authenticate API
    try:
        response = requests.post(self.__url__ + 'pod/v1/connection/create',
                                 headers=headers,
                                 data=data,
                                 cert=(self.__crt__, self.__key__),
                                 verify=True)
    except requests.exceptions.RequestException as e:
        print e
        return None
    # return the token
    return response.status_code, response.text
