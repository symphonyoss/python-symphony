#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        pod endpoint ib group methods
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@joyce.nyc'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'

import json


class Groups(object):

    def __init__(self, *args, **kwargs):
        super(Groups, self).__init__(*args, **kwargs)

    def ib_group_list(self):
        ''' ib group list '''
        req_hook = 'pod/v1/admin/group/list'
        req_args = None
        status_code, response = self.__rest__.GET_query(req_hook, req_args)
        self.logger.debug('%s: %s' % (status_code, response))
        return status_code, response

    def ib_group_member_list(self, group_id):
        ''' ib group member list '''
        req_hook = 'pod/v1/admin/group/' + group_id + '/membership/list'
        req_args = None
        status_code, response = self.__rest__.GET_query(req_hook, req_args)
        self.logger.debug('%s: %s' % (status_code, response))
        return status_code, response

    def ib_group_member_add(self, group_id, userids):
        ''' ib group member add '''
        req_hook = 'pod/v1/admin/group/' + group_id + '/membership/add'
        req_args = {'usersListId': userids}
        req_args = json.dumps(req_args)
        status_code, response = self.__rest__.POST_query(req_hook, req_args)
        self.logger.debug('%s: %s' % (status_code, response))
        return status_code, response

    def ib_group_policy_list(self):
        ''' ib group policy list '''
        req_hook = 'pod/v1/admin/policy/list'
        req_args = None
        status_code, response = self.__rest__.GET_query(req_hook, req_args)
        self.logger.debug('%s: %s' % (status_code, response))
        return status_code, response
