from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List
from lists import google_manager
from django.contrib.auth.decorators import login_required

import json


# @login_required
def home_page(request):
    # if request.method == 'POST':
    #     new_item_text = request.POST['item_text']
    #     Item.objects.create(text=new_item_text)
    #     return redirect('/lists/the-only-list-in-the-world/')

    if request.user.is_authenticated():
        return view_list(request, request.user.list.id)
    else:
        return render(request, 'lists/lists_home.html')


# @login_required
def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    # items = Item.objects.filter(list=list_)
    return render(request, 'lists/list.html', {'list': list_})


# @login_required
def new_list(request):
    list_ = List.objects.create()
    new_item_text = request.POST['item_text']
    Item.objects.create(text=new_item_text, list=list_)
    return redirect('/lists/%d/' % list_.id)

# @login_required
def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    new_item_text = request.POST['item_text']
    Item.objects.create(text=new_item_text, list=list_)
    return redirect('/lists/%d/' % list_.id)

@login_required
def google_login(request):
    redirect = '/lists/oauth2callback'
    resp = google_manager.get_login_resp(request, redirect)
    return resp


def google_auth_cb(request):
    print(request.COOKIES)
    redirect_url = request.COOKIES.get('google_auth_redirect', '/')
    print(redirect_url)
    login_ip = request.META['REMOTE_ADDR']
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        login_ip = request.META['HTTP_X_FORWARDED_FOR']
    print(login_ip)

    code = request.GET.get('code', None)
    print(code)
    if not code:
        return HttpResponse("Get code")
    info = {}
    try:
        info = google_manager.get_people_info(request, code, redirect_url)
    except Exception as e:
        return HttpResponse('No permission!!!')

    print(info)
    return HttpResponse(json.dumps(info))
