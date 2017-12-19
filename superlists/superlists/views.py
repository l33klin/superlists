#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Authors: klin
Email: l33klin@foxmail.com
Date: 2017/12/19
"""

from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    return render(request, '')

def login(request):
    return render(request, 'login.html')
