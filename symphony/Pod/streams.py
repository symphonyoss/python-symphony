#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        pod endpoint streams methods
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@joyce.nyc'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'

import json


class Streams(object):

    def __init__(self, *args, **kwargs):
        super(Streams, self).__init__(*args, **kwargs)

    def member_add(self, stream_id, user_id):
        ''' add a user to a stream '''
        req_hook = 'pod/v1/room/' + str(stream_id) + '/membership/add'
        req_args = '{ "id": %s }' % user_id
        status_code, response = self.__rest__.POST_query(req_hook, req_args)
        return status_code, response

    def member_remove(self, stream_id, user_id):
        ''' remove user from stream '''
        req_hook = 'pod/v1/room/' + str(stream_id) + '/membership/remove'
        req_args = '{ "id": %s }' % user_id
        status_code, response = self.__rest__.POST_query(req_hook, req_args)
        return status_code, response

    def create_stream(self):
        ''' create a stream '''
        req_hook = 'pod/v1/im/create'
        req_args = None
        status_code, response = self.__rest__.POST_query(req_hook, req_args)
        return status_code, response

    def create_stream_ni(self, user_ids):
        ''' create a stream in a non-inclusive manner '''
        req_hook = 'pod/v1/admin/im/create'
        req_args = json.dumps(user_ids)
        status_code, response = self.__rest__.POST_query(req_hook, req_args)
        return status_code, response

    def create_room(self, room_definition):
        ''' create's a room '''
        req_hook = 'pod/v2/room/create'
        req_args = json.dumps(room_definition)
        status_code, response = self.__rest__.POST_query(req_hook, req_args)
        return status_code, response

    def update_room(self, stream_id, room_definition):
        ''' update a room definition '''
        req_hook = 'pod/v2/room/' + str(stream_id) + '/update'
        req_args = json.dumps(room_definition)
        status_code, response = self.__rest__.POST_query(req_hook, req_args)
        return status_code, response

    def room_info(self, stream_id):
        ''' get info on room '''
        req_hook = 'pod/v2/room/' + str(stream_id) + '/info'
        req_args = None
        status_code, response = self.__rest__.GET_query(req_hook, req_args)
        return status_code, response

    def activate_stream(self, stream_id, status):
        ''' de/reactivate a stream '''
        req_hook = 'pod/v1/room/' + str(stream_id) + '/setActive?active=' + self.__rest__.bool2str(status)
        req_args = None
        status_code, response = self.__rest__.POST_query(req_hook, req_args)
        return status_code, response

    def room_members(self, stream_id):
        ''' get list of room members '''
        req_hook = 'pod/v2/room/' + str(stream_id) + '/membership/list'
        req_args = None
        status_code, response = self.__rest__.GET_query(req_hook, req_args)
        return status_code, response

    def promote_owner(self, stream_id, user_id):
        ''' promote user to owner in stream '''
        req_hook = 'pod/v1/room/' + stream_id + '/membership/promoteOwner'
        req_args = '{ "id": %s }' % user_id
        status_code, response = self.__rest__.POST_query(req_hook, req_args)
        return status_code, response

    def demote_owner(self, stream_id, user_id):
        ''' demote user to participant in stream '''
        req_hook = 'pod/v1/room/' + stream_id + '/membership/demoteOwner'
        req_args = '{ "id": %s }' % user_id
        status_code, response = self.__rest__.POST_query(req_hook, req_args)
        return status_code, response

    def search_rooms(self, query, labels=None, active=True, creator=None, skip=0, limit=25):
        ''' search rooms '''
        req_hook = 'pod/v2/room/search?skip=' + str(skip) + '&limit=' + str(limit)
        json_query = {
                       "query": query,
                       "labels": labels,
                       "active": active,
                       "creator": creator
                     }
        req_args = json.dumps(json_query)
        status_code, response = self.__rest__.POST_query(req_hook, req_args)
        return status_code, response

    def list_streams(self, types=[], inactive=False):
        ''' list user streams '''
        req_hook = 'pod/v1/streams/list'
        json_query = {
                       "streamTypes": types,
                       "includeInactiveStreams": inactive
                     }
        req_args = json.dumps(json_query)
        status_code, response = self.__rest__.POST_query(req_hook, req_args)
        return status_code, response

    def stream_info(self, stream_id):
        ''' get stream info '''
        req_hook = 'pod/v1/streams/' + stream_id + '/info'
        req_args = None
        status_code, response = self.__rest__.GET_query(req_hook, req_args)
        return status_code, response

    def stream_members(self, stream_id):
        ''' get stream members '''
        req_hook = 'pod/v1/admin/stream/' + stream_id + '/membership/list'
        req_args = None
        status_code, response = self.__rest__.GET_query(req_hook, req_args)
        return status_code, response
