#!/usr/bin/env python

import os

from setuptools import setup, find_packages

with open('requirements.txt') as requirements:
    requires = list(requirements)

setup_options = {
    'name': 'plyvelmgr',
    'version': '0.0.1',
    'description': 'Plyvel cli tool',
    'author': 'ICON Foundation',
    'author_email': 'foo@icon.foundation',
    'packages': find_packages(exclude=['tests*', 'docs']),
    'include_package_data': True,
    'py_modules': ['plyvelmgr'],
    'license': "Apache License 2.0",
    'install_requires': requires,
    'test_suite': 'tests',
    'entry_points': {
        'console_scripts': [
            'plyvelmgr=plyvelmgr:main'
        ],
    },
    'classifiers': [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6'
    ]
}

setup(**setup_options)
