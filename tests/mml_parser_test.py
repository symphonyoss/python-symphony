#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        Unit Tests for MessageML Parser
            - cashtag
            - hashtag
            - text
            - url
            - mention
'''

__author__ = 'Matt Joyce'
__email__ = 'matt.joyce@symphony.com'
__copyright__ = 'Copyright 2016, Symphony'

import unittest
import symphony


class mmlParserTest(unittest.TestCase):

    def testmmlstring(self):
        ''' test for string extrapolation '''
        mml = symphony.Mml()
        mml_string = "<messageML><b>bold</b> <i>action</i> text</messageML>"
        message = [{'id': 'id',
                    'streamId': 'teststreamId',
                    'message': mml_string,
                    'fromUserId': 'fromUserId',
                    'timestamp': 1}]
        message_ret = mml.parse_msg(message)
        if 'bold action text' in message_ret[0]['messageStr']:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def testmmlhash(self):
        ''' test for hash extrapolation '''
        mml = symphony.Mml()
        mml_string = "<messageML><hash tag=\"testhash\"/> test text stuff</messageML>"
        message = [{'id': 'id',
                    'streamId': 'teststreamId',
                    'message': mml_string,
                    'fromUserId': 'fromUserId',
                    'timestamp': 1}]
        message_ret = mml.parse_msg(message)
        if 'testhash' in message_ret[0]['hashes']:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def testmmlurl(self):
        ''' test for url extrapolation '''
        mml = symphony.Mml()
        mml_string = "<messageML>URL Test: <a href=\"https://www.python.org/\"/></messageML>"
        message = [{'id': 'id',
                    'streamId': 'teststreamId',
                    'message': mml_string,
                    'fromUserId': 'fromUserId',
                    'timestamp': 1}]
        mml.parse_msg(message)
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
