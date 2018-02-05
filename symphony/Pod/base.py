#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        pod endpoint basic methods
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@joyce.nyc'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'


class Base(object):

    def __init__(self, *args, **kwargs):
        super(Base, self).__init__(*args, **kwargs)

    def sessioninfo(self):
        ''' session info '''
        response, status_code = self.__pod__.Session.get_v2_sessioninfo(
            sessionToken=self.__session__
        ).result()
        self.logger.debug('%s: %s' % (status_code, response))
        return status_code, response
