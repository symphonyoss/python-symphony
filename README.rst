A Symphony Python Module
========================

.. image:: https://img.shields.io/pypi/v/python-symphony.svg
      :target: https://pypi.python.org/pypi/python-symphony/

.. image:: https://img.shields.io/pypi/pyversions/python-symphony.svg
      :target: https://pypi.python.org/pypi/python-symphony/

.. image:: https://img.shields.io/pypi/format/python-symphony.svg
      :target: https://pypi.python.org/pypi/python-symphony/

.. image:: https://img.shields.io/badge/license-Apache%202-blue.svg
      :target: https://github.com/symphonyoss/python-symphony/blob/master/LICENSE


The Symphony python client module provides a real-time wrapper around the Symphony REST API's to simplify the creation of chat sessions, room access, presence, messaging and more... The client provides a set of logical services representing supported features of the Symphony platform. Services support real-time events through feature based listeners and communication objects. Access is not limited to the services as all underlying Symphony client implementations are exposed for advanced use or creation of your own service.

Or it will once it's completely finished =P

Features
--------

* Parsing of p12 certificates
* Authentication
* Sending Messages
* Receiving Messages
* MessageML Parsing ( basic functionality )
* User Lookup

Requirements
------------

python-pip
openssl-dev
libgnutls-dev

Dependencies
------------

This project uses the following libraries:

* pip
* requests
* pytz
* lxml
* configparser
* bs4
* pyopenssl

----

.. _hacking guide: HACKING.rst
Check out the `hacking guide`_.
