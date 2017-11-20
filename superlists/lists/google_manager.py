#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from datetime import datetime, timedelta
from django.http import HttpResponseRedirect
from urllib.parse import urlencode
from django.conf import settings


GOOGLE_CLIENT_ID = "807816233211-qn15m8oqtl2am0ref2i4lnr3qb2uoqld.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "YC6oB_Ikv3vV_upvpAL80Qs1"
LOGIN_COOKIE_DOMAIN = "http://localhost:8000"

GOOGLE_CB_URL = "/lists/oauth2callback"

def get_redirect_url(request, is_cookies=False):
    if is_cookies:
        redirect = request.COOKIES.get('google_auth_redirect', '/')
    else:
        redirect = request.GET.get('redirect', '/')
    return redirect


def make_redirect_url(request, redirect):
    url = request.build_absolute_uri()
    pos = url.find('/', url.find('://') + 3)
    return url[:pos] + GOOGLE_CB_URL


def get_login_resp(request, redirect):
    print(redirect)
    auth_url = "https://accounts.google.com/o/oauth2/auth?" + urlencode({
        "client_id": GOOGLE_CLIENT_ID,
        "response_type": "code",
        "redirect_uri": make_redirect_url(request, redirect),
        "scope": "profile email",
        "max_auth_age": 0
    })
    resp = HttpResponseRedirect(auth_url)
    max_age = 3600 * 24
    expires = datetime.strftime(datetime.utcnow() + timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
    resp.set_cookie('google_auth_redirect', redirect, max_age=max_age, expires=expires,
                    domain=LOGIN_COOKIE_DOMAIN, secure=False)
    return resp


def get_people_info(request, code, redirect):
    resp = requests.post("https://www.googleapis.com/oauth2/v3/token?", {
        "code": code,
        "client_id": GOOGLE_CLIENT_ID, # GOOGLE_CLIENT_ID
        "client_secret": GOOGLE_CLIENT_SECRET,  # GOOGLE_CLIENT_SECERT
        "redirect_uri": make_redirect_url(request, redirect),
        "grant_type": "authorization_code"
    })
    if resp.status_code != 200:
        raise Exception('google oauth2: ' + str(resp.status_code))

    result = resp.json()
    if 'error' in result:
        raise Exception('Google oauth2: ' + result['error']['message'])

    access_token = result["access_token"]
    expiry = result["expires_in"]

    resp = requests.get("https://www.googleapis.com/plus/v1/people/me?", {
        "access_token": access_token
    })

    if resp.status_code != 200:
        raise Exception('google people.me: ' + str(resp.status_code))

    user_info = resp.json()
    if 'error' in user_info:
        raise Exception('Google oauth2: ' + user_info['error']['message'])

    email = user_info["emails"][0]['value']

    return {
        'access_token': access_token,
        'expires_in': expiry,
        'email': email,
        'display_name': user_info['displayName'],
        'image': user_info['image']['url']
    }
