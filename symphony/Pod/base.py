#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        pod methods
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@nycresistor.com'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'

import json
import requests


def get_userid_by_email(self, email):
    ''' get userid by email '''
    headers = {'content-type': 'application/json',
               'sessionToken': self.__session__}

    # HTTP POST query to keymanager authenticate API
    try:
        response = requests.get(self.__url__ + 'pod/v1/user?email=' + email,
                                headers=headers,
                                cert=(self.__crt__, self.__key__),
                                verify=True)
    except requests.exceptions.RequestException as e:
        print e
        return None
    # load json response as list
    userid = json.loads(response.text)
    # return the token
    return userid['id']


def get_user_id_by_user(self, username):
    ''' get user id by username '''
    headers = {'content-type': 'application/json',
               'sessionToken': self.__session__}

    # HTTP POST query to search rooms
    try:
        response = requests.get(self.__url__ + 'pod/v1/user/name/' + username + '/get',
                                headers=headers,
                                cert=(self.__crt__, self.__key__),
                                verify=True)
    except requests.exceptions.RequestException as e:
        print e
        return None

    # load json response as list
    string = json.loads(response.text)
    # return the token
    return string['id']


def adduser_to_stream(self, streamid, userid):
    ''' add a user to a stream '''
    headers = {'Content-Type': 'application/json',
               'sessionToken': self.__session__,
               'keyManagerToken': self.__keymngr__}

    data = '{ "id": %s }' % userid

    # HTTP POST query to keymanager authenticate API
    try:
        response = requests.post(self.__url__ + 'pod/v1/room/' + streamid + '/membership/add',
                                 headers=headers,
                                 data=data,
                                 cert=(self.__crt__, self.__key__),
                                 verify=True)
    except requests.exceptions.RequestException as e:
        print e
        return None
    # return the token
    return response.status_code, response.text


def user_feature_update(self, userid):
    ''' update features by user id '''
    headers = {'content-type': 'application/json',
               'sessionToken': self.__session__,
               'keyManagerToken': self.__keymngr__}
    # you can add as many entitlements as you want here
    data = '[{"entitlment": "isExternalRoomEnabled", "enabled": true },'\
           '{"entitlment": "isExternalIMEnabled", "enabled": true }]'

    # HTTP POST query to search rooms
    try:
        response = requests.post(self.__url__ + 'pod/v1/admin/user/' + str(userid) + '/features/update',
                                 headers=headers,
                                 data=data,
                                 cert=(self.__crt__, self.__key__),
                                 verify=True)
    except requests.exceptions.RequestException as e:
        print e
        return None

    # return the token
    return response.status_code, response.text


def search_user(self, search_str, search_filter, local):
    ''' add a user to a stream '''
    headers = {'Content-Type': 'application/json',
               'sessionToken': self.__session__}

    data = {
        "query": search_str,
        "filters": search_filter
    }
    data = json.dumps(data)

    try:
        response = requests.post(self.__url__ + 'pod/v1/user/search?local=' + local,
                                 headers=headers,
                                 data=data,
                                 cert=(self.__crt__, self.__key__),
                                 verify=True)
    except requests.exceptions.RequestException as e:
        print e
        return None
    return response.status_code, response.text
