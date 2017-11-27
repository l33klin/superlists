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


proxies = {'http': 'http://127.0.0.1:7777',
           'https': 'http://127.0.0.1:7777'}


class ProxyRequests(object):
    """
    Use local port 7777 as proxy, Only support stateless request
    """

    @staticmethod
    def post(url, data=None, json=None, **kwargs):
        requests.post(url, data=data, json=json, proxy=proxies, **kwargs)

    @staticmethod
    def get(url, params=None, **kwargs):
        requests.get(url, params=params, proxy=proxies, **kwargs)

    @staticmethod
    def options(url, **kwargs):
        requests.options(url, proxy=proxies, **kwargs)

    @staticmethod
    def head(url, **kwargs):
        requests.head(url, proxy=proxies, **kwargs)

    @staticmethod
    def put(url, data=None, **kwargs):
        requests.put(url, data=data, proxy=proxies, **kwargs)

    @staticmethod
    def patch(url, data=None, **kwargs):
        requests.patch(url, data=data, proxy=proxies, **kwargs)

    @staticmethod
    def delete(url, **kwargs):
        requests.delete(url, proxy=proxies, **kwargs)
