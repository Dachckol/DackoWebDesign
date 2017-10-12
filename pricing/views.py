from django.shortcuts import render_to_response
from django.template import RequestContext
from pricing.models import Package


def home(request):
    template = "pricing.html"
    packages = Package.objects.all()
    context = {"packages": packages}
    return render_to_response(template, context, context_instance=RequestContext(request))
