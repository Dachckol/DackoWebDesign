from django.shortcuts import render_to_response
from portfolio.models import Website
from pricing.models import Package
from django.template import RequestContext


def home(request):
    websites = Website.objects.all()
    context = {"websites": websites}
    template = "index.html"
    return render_to_response(template,
                              context,
                              context_instance=RequestContext(request))


def about(request):
    context = {}
    template = "about.html"
    return render_to_response(template, context)


def portfolio(request):
    websites = Website.objects.all()
    context = {"websites": websites}
    template = "portfolio.html"
    return render_to_response(template,
                              context,
                              context_instance=RequestContext(request))


def pricing(request):
    packages = Package.objects.all()
    context = {"packages": packages}
    template = "pricing.html"
    return render_to_response(template,
                              context,
                              context_instance=RequestContext(request))


def faq(request):
    context = {}
    template = "faq.html"
    return render_to_response(template, context)


def learning(request):
    context = {}
    template = "learning.html"
    return render_to_response(template, context)


def contact(request):
    context = {}
    template = "contact.html"
    return render_to_response(template, context)
