from django.shortcuts import render
from django.http import HttpResponse
import json
import pprint

# Create your views here.
def index(request):
  pp = pprint.PrettyPrinter()
  pp.pprint(request.GET.get('bla'))
  return HttpResponse("Hello, world. You're at the polls index.")