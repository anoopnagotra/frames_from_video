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
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt 
def get_circle(request):
	import numpy as np
	import cv2
	cap = cv2.VideoCapture('cells.mp4')
	size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
	
	import shutil 
	import os 
	frame_path = settings.PATH+ "/static/video/"
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

	fourcc = cv2.VideoWriter_fourcc(*'DIVX')
	video = cv2.VideoWriter(str(frame_path)+'/6.avi', fourcc, 25, size)
	print(":I am hree")
	# while(True):
	#
	#     ret, frame = cap.read()
	#
	#
	#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#     gray = cv2.medianBlur(gray,5)
	#     cimg = frame.copy()
	#     circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 10, np.array([]), 200, 100, 100, 200)
	#     if circles == 1:
	#         print('Circle true')
	#     else:
	#         print('No circle')
	#     cv2.imshow('video',gray)
	#
	#     if cv2.waitKey(1) & 0xFF == ord('q'):
	#         break
	#
	#
	# cap.release()
	# cv2.destroyAllWindows()
	while(1):
	    ret, frame = cap.read()
	    if not ret:
	        break
	    frame = cv2.convertScaleAbs(frame)
	    params = cv2.SimpleBlobDetector_Params()
	    params.blobColor = 255
	    params.filterByColor = True
	    params.minArea = 0
	    params.filterByArea = True
	    params.filterByCircularity= False
	    params.filterByInertia= True
	    params.minThreshold = 120;
	    params.maxThreshold = 255;
	    ver = (cv2.__version__).split('.')
	    if int(ver[0]) < 3:
	        detector = cv2.SimpleBlobDetector(params)
	    else:
	        detector = cv2.SimpleBlobDetector_create(params)
	    keypoints = detector.detect(frame)
	    im_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
	    if ret == True:
	        video.write(im_with_keypoints)
	        # cv2.imshow('frame', im_with_keypoints)
	    else:
	        cap.release()
	        break
	    k = cv2.waitKey(10) & 0xff
	    if k == 27:
	        break
	print("I am dob=ne")
	response = HttpResponse(json.dumps({ 'status':1, 'msg':'File received', 'images':"images"}), content_type='application/json')
	response.status_code = 200
	return response	