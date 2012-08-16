# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from datetime import datetime
from main_code.models import *
import json

uploads_root = '/uploads/'

def home(request):
    print request
    return HttpResponse("Hello, main woodland")

def hello(request):
    print request
    return HttpResponse("Hello, main woodland")

from django import forms
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

def test_file(request):
    #return HttpResponse('hello, file upload test')
    context = RequestContext(request)
    return render_to_response('file_upload.html', context)

def test_file_upload(request):
    fc = ''
    if request.method == 'POST':
        files = request.FILES
        if files.has_key('myfile'):
            fc = files['myfile']
            f = open('./'+fc.name, 'w')
            if fc.multiple_chunks:
                for c in fc.chunks():
                    f.write(c)
            else:
                f.write(fc.read())
            f.close()
    print 'hello'
    print fc
    #print request.FILES
    return HttpResponse("hello, file")

######################### main code #################

def request_get(param, key):
    return param.get(key, None)

def photo_upload(request):
    print request
    errors = []
    title = ''
    path = ''
    tags = ''
    lat = ''
    lng = ''
    user_name = request.REQUEST.get('myusername', None)
    if user_name == None:
        error = 'myusername is empty'
        errors.append(error)
    else:
        try:
            user = User.objects.get(username=user_name)
            print user
        except Exception as e:
            error = 'myusername is wrong: '+e
            errors.append(error)
    desc = ''
    fs = ''
    if request.method == 'POST':
        fs = request.FILES
        if fs.has_key('myphoto'):
            fs = fs['myphoto']
            if fs == None or fs == '':
                error = 'request "myphoto" is empty'
                errors.append(error)
            else:
                now = datetime.now()
                path = uploads_root+str(now)+"_"+fs.name
                path = path.replace(':', '_')
                path = path.replace(' ', '_')
                print path
                f = open('.'+path, 'w')
                if fs.multiple_chunks:
                    for c in fs.chunks():
                        f.write(c)
                else:
                    f.write(fs.read())
                f.close()
        else:
            error = 'request does not have "myphoto" argument as file'
            errors.append(error)
    else:
        error = 'request method should be POST'
        errors.append(error)
    title = request.REQUEST.get('photo_title', None)
    tags = request.REQUEST.get('photo_tags', None)
    lat = request.REQUEST.get('photo_lat', None)
    lng = request.REQUEST.get('photo_lng', None)
    desc = request.REQUEST.get('photo_desc', None)
    return_format = request.REQUEST.get('return_format', None)
    if title == None or title == '':
        error = 'photo_title is empty'
        errors.append(error)
    if tags == None or tags == '':
        error = 'photo_tags is empty'
        errors.append(error)
    if lat == None or lat == '':
        error = 'photo_lat is empty'
        errors.append(error)
    if lng == None or lng == '':
        error = 'photo_lng is empty'
        errors.append(error)
    if desc == None or desc == '':
        error = 'photo_desc is empty'
        errors.append(error)
    r = {}
    if len(errors) != 0:
        r['status'] = 'bad'
        r['errors'] = errors
    else:
        p, created = UploadFile.objects.get_or_create(user=user, type=0, name=title, path=path, lat=lat, lng=lng, desc=desc)
        p.save()
        ts = tags.split(',')
        for t in ts:
            tag, created = Tag.objects.get_or_create(name=t)
            p.tags.add(tag)
        p.save()
        p_path = p.path
        p_id = p.id
        r['status'] = 'good'
        r['result'] = {'id':p_id, 'path':p_path}
    rs = json.dumps(r)
    return HttpResponse(rs)
    '''if len(errors) > 0: # if not debug, it would return json
    #    c = {
            "errors": errors,
            }
        print c
        context = RequestContext(requests, c)
        return render_to_response('file_upload.html', context)
    '''
    #url = '/main/photo_view'
    #return HttpResponseRedirect(url)

#@login_required
def photo_view(request):
    print request
    user_name = request.REQUEST.get('myusername', None)
    r = {}
    errors = []
    if user_name == None:
        error = 'myusername is empty'
        errors.append(error)
    else:
        try:
            user = User.objects.get(username=user_name)
            print user
        except Exception as e:
            error = 'myusername is wrong: '+e
            errors.append(error)
    if len(errors) != 0:
        r['status'] = 'bad'
        r['error'] = errors
        rs = json.dumps(r)
        return HttpResponse(rs)
    #user = request.user
    ps = photo_view_get(user)
    r['status'] = 'good'
    r['result'] = ps
    rs = json.dumps(r)
    return HttpResponse(rs)

def photo_view_get(user):
    photos = UploadFile.objects.filter(user=user)
    print photos
    ps = []
    for photo in photos:
        print photo
        path = photo.path
        name = photo.name
        time = photo.time_created
        lat = photo.lat,
        lng = photo.lng,
        desc = photo.desc
        tags_fields = photo.tags.all()
        tags = ''
        for t in tags_fields:
            t_name = t.name
            tags = tags+","+t_name # should i add url on it?
        username = user.username
        p = {
            'path':path,
            'name':name,
            'time':str(time),
            'user':username,
            'lat':lat,
            'lng':lng,
            'desc':desc,
            'tags':tags
            }
        ps.append(p)
    return ps


def photo_comment_view(request):
    return HttpResponse('photo comment')

def comment_make(request):
    return HttpResponse('comment make')


######################## demo purpose ##################
#@login_required
def demo_photo_upload(request):
    c = {}
    context = RequestContext(request, c)
    return render_to_response('file_upload.html', context)

def demo_photo_view(request):
    print request
    user_name = request.REQUEST.get('myusername', None)
    r = {}
    errors = []
    if user_name == None:
        error = 'myusername is empty'
        errors.append(error)
    else:
        try:
            user = User.objects.get(username=user_name)
            print user
        except Exception as e:
            error = 'myusername is wrong: '+e
            errors.append(error)
    if len(errors) != 0:
        r['status'] = 'bad'
        r['error'] = errors
        rs = json.dumps(r)
        return HttpResponse(rs)
    #user = request.user
    ps = photo_view_get(user)
    c = {
        'photos': ps
        }
    print c
    context = RequestContext(request, c)
    return render_to_response('file_view.html', context)

def demo_comment_make(request):
    return HttpResponse('hello')
