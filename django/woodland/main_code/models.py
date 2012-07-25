from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def dict_to_choices(d):
    choices = []
    i = 1
    for k, v in d.iteritems():
        choice = (i, v)
        choices.append(choice)
        i = i+1
    return choices


UPLOAD_TYPE = {
    'image':"IMAGE",
    'file':"FILE",
    }
UPLOAD_TYPE_CHOICES = dict_to_choices(UPLOAD_TYPE)

class Tag(models.Model):
    name = models.CharField(max_length=126, null=True)
    desc = models.CharField(max_length=512, null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True)
    def __unicode__(self):
        return 'Tag: %s'%(self.name)

class Ptjt(models.Model):
    ptjt_id = models.IntegerField(max_length=8, null=True)
    name = models.CharField(max_length=256, null=True)
    desc = models.CharField(max_length=512, null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    lat = models.CharField(max_length=256, null=True)
    lng = models.CharField(max_length=256, null=True)
    tag = models.ManyToManyField(Tag, null=True)
    user = models.ForeignKey(User, null=True)
    def __unicode__(self):
        return 'PTJT:%s'%(self.name)

class UploadFile(models.Model):
    type = models.IntegerField(max_length=2, choices=UPLOAD_TYPE_CHOICES)
    name = models.CharField(max_length=256, null=True)
    path = models.CharField(max_length=256, null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True)
    lat = models.CharField(max_length=256, null=True)
    lng = models.CharField(max_length=256, null=True)
    desc = models.CharField(max_length=512, null=True)
    tags = models.ManyToManyField(Tag, null=True)
    def __unicode__(self):
        return 'File:%s'%(self.name)

class Comment(models.Model):
    root_file = models.ForeignKey(UploadFile, null=True)
    parent_comment = models.ForeignKey('self', null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True)
    lat = models.CharField(max_length=256, null=True)
    lng = models.CharField(max_length=256, null=True)
    content = models.CharField(max_length=512, null=True)
    tags = models.ManyToManyField(Tag, null=True)
    def __unicode__(self):
        return 'Comment:%s'%(content)
    

