#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        Abstracted GET / POST calls
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@joyce.nyc'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'

import requests


class PKCS(object):

    def __init__(self, *args, **kwargs):
        super(PKCS, self).__init__(*args, **kwargs)

    def PKCS_GET_query(self, req_hook, req_args):
        ''' Generic GET query method '''
        # GET request methods only require sessionTokens
        headers = {'content-type': 'application/json',
                   'sessionToken': self.__session__}

        # HTTP GET query method using requests module
        try:
            if req_args is None:
                response = requests.get(self.__url__ + req_hook,
                                        headers=headers,
                                        cert=(self.__crt__, self.__key__),
                                        verify=True)
            else:
                response = requests.get(self.__url__ + req_hook + str(req_args),
                                        headers=headers,
                                        cert=(self.__crt__, self.__key__),
                                        verify=True)
        except requests.exceptions.RequestException as err:
            self.logger.error(err)
            return '500', 'Internal Error in PKCS_RESTful.GET_query()'
        # return the token
        self.logger.debug('%s: %s' % (response.status_code, response.text))
        return response.status_code, response.text

    def PKCS_POST_query(self, req_hook, req_args):
        ''' Generic POST query method '''
        # HTTP POST queries require keyManagerTokens and sessionTokens
        headers = {'Content-Type': 'application/json',
                   'sessionToken': self.__session__,
                   'keyManagerToken': self.__keymngr__}

        # HTTP POST query to keymanager authenticate API
        try:
            if req_args is None:
                response = requests.post(self.__url__ + req_hook,
                                         headers=headers,
                                         cert=(self.__crt__, self.__key__),
                                         verify=True)
            else:
                response = requests.post(self.__url__ + req_hook,
                                         headers=headers,
                                         data=req_args,
                                         cert=(self.__crt__, self.__key__),
                                         verify=True)
        except requests.exceptions.RequestException as err:
            self.logger.error(err)
            return '500', 'Internal Error in PKCS_RESTful.POST_query()'
        # return the token
        self.logger.debug('%s: %s' % (response.status_code, response.text))
        return response.status_code, response.text
