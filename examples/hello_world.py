#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    hello world for symphony
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@joyce.nyc'
__copyright__ = 'Copyright 2017, Symphony'

import symphony
import sys


def main():
    ''' main program loop '''
    conn = symphony.Config('/path/to/config/file')
    # connect to pod
    try:
        agent, pod, symphony_sid = conn.connect()
    except Exception as err:
        print('failed to connect to symphony: %s' % (err))
        sys.exit(1)
    # get datafeed
    try:
        datafeed_id = agent.create_datafeed()
        print(datafeed_id)
    except Exception as err:
        print('failed to allocate datafeed id: %s' % (err))
        sys.exit(1)
    # main loop
    msgFormat = 'MESSAGEML'
    message = '<messageML> hello world. </messageML>'
    # send message
    retstring = agent.send_message(symphony_sid, msgFormat, message)
    print(retstring)


if __name__ == "__main__":
    main()
