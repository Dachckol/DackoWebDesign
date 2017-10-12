from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
    template = "home.html"
    context = {}
    return render_to_response(template, context, context_instance=RequestContext(request))


def about(request):
    template = "about.html"
    context = {}
    return render_to_response(template, context, context_instance=RequestContext(request))


def faq(request):
    template = "faq.html"
    context = {}
    return render_to_response(template, context, context_instance=RequestContext(request))
