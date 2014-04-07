# -*- encoding: utf8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from intro.introapp.models import Post

def index(request, key="", tag=""):
    # Get all posts from DB
    if key == "":
      posts = Post.objects.all()
    else:
      posts = Post.objects.filter(**{key+"__contains" : tag })

    return render_to_response('index.html', {'Posts': posts},
                              context_instance=RequestContext(request))
    