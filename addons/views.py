# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response

def home(request):
    ctx = {}
    return render_to_response(
        '__site__/rootpage.html',
        ctx, context_instance=RequestContext(request))
