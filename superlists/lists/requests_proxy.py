#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Time    : 2017/11/27 下午6:45
@Author  : Jian
@Contact : l33klin@gmail.com
@Site    : 
@File    : requests_proxy.py
"""

import requests
from functools import wraps


proxies = {'http': 'http://127.0.0.1:7777',
           'https': 'http://127.0.0.1:7777'}


class MultiProxyException(Exception):

    def __init__(self, *args, **kwargs):
        pass

    @staticmethod  # known case of __new__
    def __new__(*args, **kwargs):  # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


def proxy_check(func):

    @wraps(func)
    def function_check(*args, **kwargs):
        if 'proxy' in kwargs:
            raise MultiProxyException("More than one proxy argument is passed!")
        result = func(*args, **kwargs)
        return result

    return function_check


class ProxyRequests(object):
    """
    Use local port 7777 as proxy, Only support stateless request
    """

    @staticmethod
    @proxy_check
    def post(url, data=None, json=None, **kwargs):
        requests.post(url, data=data, json=json, proxy=proxies, **kwargs)

    @staticmethod
    @proxy_check
    def get(url, params=None, **kwargs):
        requests.get(url, params=params, proxy=proxies, **kwargs)

    @staticmethod
    @proxy_check
    def options(url, **kwargs):
        requests.options(url, proxy=proxies, **kwargs)

    @staticmethod
    @proxy_check
    def head(url, **kwargs):
        requests.head(url, proxy=proxies, **kwargs)

    @staticmethod
    @proxy_check
    def put(url, data=None, **kwargs):
        requests.put(url, data=data, proxy=proxies, **kwargs)

    @staticmethod
    @proxy_check
    def patch(url, data=None, **kwargs):
        requests.patch(url, data=data, proxy=proxies, **kwargs)

    @staticmethod
    @proxy_check
    def delete(url, **kwargs):
        requests.delete(url, proxy=proxies, **kwargs)
