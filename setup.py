#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0', 'requests',
    # TODO: put package requirements here
]

setup_requirements = [
    # TODO(delneg): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='bitfinex_api',
    version='0.1.0',
    description="AModern Python wrapper for Bitfinex api v1 & v2",
    long_description=readme + '\n\n' + history,
    author="Denis Bobrov",
    author_email='delneg@yandex.ru',
    url='https://github.com/delneg/bitfinex_api',
    packages=find_packages(include=['bitfinex_api']),
    entry_points={
        'console_scripts': [
            'bitfinex_api=bitfinex_api.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='bitfinex_api',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
