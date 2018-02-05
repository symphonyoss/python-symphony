#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        Agent API Methods
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@joyce.nyc'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'


class Base(object):

    def __init__(self, *args, **kwargs):
        super(Base, self).__init__(*args, **kwargs)

    def test_echo(self, test_string):
        ''' echo test '''
        response, status_code = self.__agent__.Util.post_v1_util_echo(
            sessionToken=self.__session__,
            keyManagerToken=self.__keymngr__,
            echoInput={"message": test_string}
        ).result()
        self.logger.debug('%s: %s' % (status_code, response))
        return status_code, response

    def create_datafeed(self):
        ''' create datafeed '''
        response, status_code = self.__agent__.Datafeed.post_v4_datafeed_create(
            sessionToken=self.__session__,
            keyManagerToken=self.__keymngr__
        ).result()
        # return the token
        self.logger.debug('%s: %s' % (status_code, response))
        return status_code, response['id']

    def read_datafeed(self, datafeed_id):
        ''' get datafeed '''
        response, status_code = self.__agent__.Datafeed.get_v4_datafeed_id_read(
            sessionToken=self.__session__,
            keyManagerToken=self.__keymngr__,
            id=datafeed_id
        ).result()
        self.logger.debug('%s: %s' % (status_code, response))
        return status_code, response

    def send_message(self, threadid, msgFormat, message):
        ''' send message to threadid/stream '''
        # using deprecated v3 message create because of bug in codegen of v4 ( multipart/form-data )
        response, status_code = self.__agent__.Messages.post_v3_stream_sid_message_create(
            sessionToken=self.__session__,
            keyManagerToken=self.__keymngr__,
            sid=threadid,
            message={"format": msgFormat,
                     "message": message}
        ).result()
        self.logger.debug('%s: %s' % (status_code, response))
        return status_code, response

    def read_stream(self, stream_id, since_epoch):
        ''' get datafeed '''
        response, status_code = self.__agent__.Messages.get_v4_stream_sid_message(
            sessionToken=self.__session__,
            keyManagerToken=self.__keymngr__,
            sid=stream_id,
            since=since_epoch
        ).result()
        self.logger.debug('%s: %s' % (status_code, response))
        return status_code, response
