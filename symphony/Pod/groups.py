'''
    Purpose:
        pod endpoint ib group methods
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@nycresistor.com'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'

import json


def ib_group_list(self):
    ''' ib group list '''
    req_hook = 'pod/v1/admin/group/list'
    req_args = None
    status_code, response = self.__rest__.GET_query(req_hook, req_args)
    return status_code, json.loads(response)


def ib_group_member_list(self, group_id):
    ''' ib group member list '''
    req_hook = 'pod/v1/admin/group/' + group_id + '/membership/list'
    req_args = None
    status_code, response = self.__rest__.GET_query(req_hook, req_args)
    return status_code, json.loads(response)


def if_group_member_add(self, group_id, userids):
    req_hook = 'pod/v1/admin/group/' + group_id + '/membership/add'
    req_args = {'usersListId': userids}
    status_code, response = self.__rest__.POST_query(req_hook, req_args)
    return status_code, response


def ib_group_policy_list(self):
    req_hook = 'pod/v1/admin/policy/list'
    req_args = None
    status_code, response = self.__rest__.GET_query(req_hook, req_args)
    return status_code, json.loads(response)
