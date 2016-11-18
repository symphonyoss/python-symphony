#!/usr/bin/env python

'''
    Execution:
        python setup.py build
        python setup.py install
    Purpose:
        This is the setup script for the app
'''

__author__ = 'Matt Joyce'
__email__ = 'matt.joyce@symphony.com'
__copyright__ = "Copyright 2016, Symphony"

from setuptools import setup, find_packages
from pip.req import parse_requirements


# parse_requirements() returns generator of
# pip.req.InstallRequirement objects
install_reqs = parse_requirements('requirements.txt',
                                  session=False)

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='python-symphony',
    version='0.0.1',
    description='python module for symphony chat',
    author='Engineering Services',
    author_email='symphony-engservices@symphony.com',
    url='https://symphony.engineering/',
    # install dependencies from requirements.txt
    install_requires=reqs,
    packages=find_packages(),
    # bin files / python standalone executable scripts
    include_package_data=True,
    zip_safe=False,
)
