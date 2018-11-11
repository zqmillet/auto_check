#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='auto_checker',
    version=1.0,
    description=(
        'a decorator can auto check the function arguments'
    ),
    long_description=open('README.rst').read(),
    author='zhangqi',
    author_email='zqmillet@qq.com',
    maintainer='zhangqi',
    maintainer_email='zqmillet@qq.com',
    license='BSD License',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/zqmillet/auto_check',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
)
