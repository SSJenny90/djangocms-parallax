#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

REPO_URL = "https://github.com/SSJenny90/django-cms-parallax"

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='Django CMS Parallax',
    packages=find_packages(),
    include_package_data=True,
    version=0.0.1,
    author='Sam Jennings',
    license='MIT',
    description='Django CSM integration for parallax.js',
    url=REPO_URL,
    install_requires=[
        "Django",
    ],
    keywords='parallax django djangocms',
    classifiers=[
        'Development Status :: 1 - Development',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'Natural Language :: English',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
