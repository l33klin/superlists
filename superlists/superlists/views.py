#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Authors: klin
Email: l33klin@foxmail.com
Date: 2017/12/19
"""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def home(request):
    if request.user.is_authenticated():
        # Do something for authenticated users.
        print("authenticated user")
    else:
        # Do something for anonymous users.
        print("AnonymousUser")
    return render(request, 'home.html')
