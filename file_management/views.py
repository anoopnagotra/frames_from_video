from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.loader import render_to_string
from django.core import serializers
from pprint import pprint 
import re
from django.db.models import Q

# from models import User
import json
import datetime

def custom_page_not_found_view(request, exception):
    return render(request, "error/400.html", {})

def custom_error_view(request, exception=None):
	pprint("dshdsg")
	return render(request, "error/500.html", {})

def custom_permission_denied_view(request, exception=None):
	pprint("dshg")
	return render(request, "error/403.html", {})

def custom_bad_request_view(request, exception=None):
	pprint("dshg")
	return render(request, "error/4s00.html", {})
	# return render(request, "error/400.html", {})

