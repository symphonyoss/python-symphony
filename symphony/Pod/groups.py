'''
    Purpose:
        pod endpoint group methods
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@nycresistor.com'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'

import json


def group_list(self):
    ''' group list '''
    req_hook = 'pod/v1/admin/group/list'
    req_args = None
    status_code, response = self.__rest__.GET_query(req_hook, req_args)
    return json.loads(response)
