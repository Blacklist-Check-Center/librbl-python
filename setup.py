#!/bin/venv/python

from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
   name='librbl',
   version='0.1~all',
   license="GPLv3",
   long_description=long_description,
   description='A library to check if a domain or an ip is blacklisted',
   author='Julien Gomes Dias',
   author_email='abld@abld.info',
   packages=['librbl']
)
