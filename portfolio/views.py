from django.shortcuts import render_to_response
from django.template import RequestContext
from portfolio.models import Website


def home(request):
    template = "portfolio.html"
    websites = Website.objects.all()
    context = {"websites": websites}
    return render_to_response(template, context, context_instance=RequestContext(request))
