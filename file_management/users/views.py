from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from file_management.users.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
import os 
from django.core.files.storage import FileSystemStorage

# from models import User
import json
import datetime

STATES = {
		'BW': 'Baden-Württemberg',
        'BY': 'Bayern',
        'BE': 'Berlin',
        'BB': 'Brandenburg',
        'HB': 'Bremen',
        'HH':'Hamburg',
        'HE': 'Hessen',
        'MV': 'Mecklenburg-Vorpommern',
        'NI': 'Niedersachsen',
        'NW': 'Nordrhein-Westfalen',
        'RP': 'Rheinland-Pfalz',
        'SL': 'Saarland',
        'SN': 'Sachsen',
        'ST': 'Sachsen-Anhalt',
        'SH': 'Schleswig-Holstein',
        'TH':'Thüringen'
        }
"""
Method:             home
Developer:          Anoop Kumar
Created Date:       24-03-2020
Purpose:            Home
Params:             null
Return:             null
"""
# @login_required
def home(request):
	return render(request, 'home/index.html', {})
"""end function dashboard"""

"""
Method:             home
Developer:          Anoop Kumar
Created Date:       24-03-2020
Purpose:            Home
Params:             null
Return:             null
"""
# @login_required


def get_frames(request):
	name = request.GET.get('name', None)
	path = settings.DIRECTORY + name
	frame_path= settings.DIRECTORY + "frames/"


	import shutil 
	import os 
	frame_path = settings.PATH+ "/static/frames/"
	print("BASE_DIR")
	print(frame_path)
	print(settings.PATH)
	print(frame_path)
	print("get-frames inside")
	

	if not os.path.exists(frame_path):
		print("Here")
		try:
		    os.makedirs(frame_path)
		    print( "Directory created ")
		except FileExistsError:
		    print("Directory " , frame_path ,  " already exists")
		    pass
	else:
		print("THere")
		shutil.rmtree(frame_path)
		print("deleted")
		os.makedirs(frame_path)
		print( "Again Directory created ")
	# return render(request, 'backend/dashboard/index2.html', {"dashboard": "active"})

	import cv2
	# Path to video file 
	vidObj = cv2.VideoCapture(path)
	print("==============>>>>>>>>>>>> ")
	print("vidObj >> ", vidObj)
	# Used as counter variable 
	count = 0
	# checks whether frames were extracted 
	success = 1
	images = []
	while success:
		data = {}
		# vidObj object calls read
		# function extract frames
		success, image = vidObj.read()
		# print(count, image)
		# Saves the frames with frame-count
		count += 1
		if count <= 500:

			cv2.imwrite(frame_path+"frame%d.jpg" % count, image)
			# images.append(str(frame_path)+"frame"+str(count)+".jpg")
			images.append("frame"+str(count)+".jpg")
		else:
			break
	print(images)
	response = HttpResponse(json.dumps({ 'status':1, 'msg':'File received', 'images':images}), content_type='application/json')
	response.status_code = 200
	return response	
"""end function dashboard"""
