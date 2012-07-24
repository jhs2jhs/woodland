# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

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
