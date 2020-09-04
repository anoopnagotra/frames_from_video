from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from file_management.users.models import User, MyVideo
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
import os 
from django.core.files.storage import FileSystemStorage

# from models import User
import json
import datetime
import shutil 
import os 

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
	data = MyVideo.objects.all()
	return render(request, 'home/index.html', {'video':data})
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
from django.core.files.storage import FileSystemStorage
def upload_video(request):
	print("==========================")
	file =  request.FILES.get('video')
	# directory = settings.DIRECTORY + request.user.username +"/profile"
	# directory= settings.DIRECTORY 
	directory= settings.PATH + "/static/"
	print(directory)
	print(file)
	if file:
		file_type = file.content_type.split('/')[0]
		print(file_type)
		file_name = file.name
		# directory = settings.DIRECTORY + request.user.username +"/profile"
		if not os.path.exists(directory):
			try:
			    os.makedirs(directory)
			except FileExistsError:
			    print("Directory " , directory ,  " already exists")
			    pass
		# exit()
		if file_type == 'video':
			name = file.name
			path = directory.split('/')
			print(path)
			path = path[-3:]
			path = '/'.join([str(i) for i in path])
			fs = FileSystemStorage()
			print(" \n Path >>> ")
			print(path)
			fs.base_location = directory
			try:
				filename = fs.save(name, file)
			except Exception as e:
				print(e)

			print(filename)
			MyVideo.objects.all().delete()
			video = MyVideo()
			video.title = filename
			video.full_path = path
			video.save()
			print("video is saved")
	return redirect('/')

def get_shape(request):
	name = request.GET.get('name', None)
	image_path = settings.PATH + name
	# /home/meetu/p_p/frames_from_video/static/frames/frame55.jpg
	print("oaky hai sb")
	print(image_path)



	import numpy as np
	import cv2

	# im = cv2.imread('sun0016.bmp')
	# im = cv2.imread('squares2.PNG')
	im = cv2.imread(image_path)
	# im = cv2.imread('center.jpg')
	height, width, depth = im.shape
	print (height, width, depth)
	thresh = 132
	imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(imgray,(5,5),0)
	edges = cv2.Canny(blur,thresh,thresh*2)
	# contours, hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	_, contours, _= cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnt = contours[0]
	cv2.drawContours(im,contours,-1,(119,119,119),-1)

	#centroid_x = M10/M00 and centroid_y = M01/M00
	M = cv2.moments(cnt)
	x = int(M['m10']/M['m00'])
	y = int(M['m01']/M['m00'])
	# exit()
	print (x,y)
	print (width/2.0,height/2.0)
	print (width/2-x,height/2-y)


	cv2.circle(im,(x,y),1,(0,0,255),2)

	cv2.putText(im,"center of Sun contour", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255))

	cv2.circle(im,(int(width/2),int(height/2)),1,(255,0,0),2)

	cv2.putText(im,"center of image", (int(width/2),int(height/2)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0))

	# cv2.imshow('contour',im)

	frame_path = settings.PATH+ "/static/shape/"

	if not os.path.exists(frame_path):
		print("\nHere")
		try:
		    os.makedirs(frame_path)
		    print( "\nDirectory created ")
		except FileExistsError:
		    print("\nDirectory " , frame_path ,  " already exists")
		    pass
	else:
		print("\nTHere in Else \n")
		shutil.rmtree(frame_path)
		print("deleted")
		os.makedirs(frame_path)
		print( "Again Directory created ")

	cv2.imwrite(frame_path+"img_shape.png", im)

	cv2.waitKey(0)
	response = HttpResponse(json.dumps({ 'status':1, 'msg':'File received', 'images':"images"}), content_type='application/json')
	response.status_code = 200
	return response	

def get_frames(request):
	name = request.GET.get('name', None)
	# path = settings.DIRECTORY + name
	# directory= settings.PATH + "/static/"
	path = settings.PATH + "/static/"+name
	frame_path= settings.DIRECTORY + "frames/"


	import shutil 
	import os 
	frame_path = settings.PATH+ "/static/frames/"
	print("*************************\nBASE_DIR\n")
	print(path)
	print(settings.PATH)
	print(frame_path)
	print("\nget-frames inside")
	

	if not os.path.exists(frame_path):
		print("\nHere")
		try:
		    os.makedirs(frame_path)
		    print( "\nDirectory created ")
		except FileExistsError:
		    print("\nDirectory " , frame_path ,  " already exists")
		    pass
	else:
		print("\nTHere in Else \n")
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
		print("te >>>>  Here")
		data = {}
		# vidObj object calls read
		# function extract frames
		success, image = vidObj.read()
		print(count, image)
		# Saves the frames with frame-count
		count += 1
		if count <= 100:
			print("updating image data Here")
			cv2.imwrite(frame_path+"frame%d.png" % count, image)
			# images.append(str(frame_path)+"frame"+str(count)+".jpg")
			images.append("frame"+str(count)+".png")
		else:
			break
	print(images)
	print("oaky hai sb")
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