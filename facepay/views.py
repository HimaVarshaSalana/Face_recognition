
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages

from django.contrib.auth.models import User
from users.models import CardDetails

import sys
from subprocess import run,PIPE

import face_recognition
import cv2

# Create your views here.
def home(request):
    return render(request,'facepay/home.html')

def about(request):
    return render(request,'facepay/about.html')

def mobilepay(request):
    return render(request,'facepay/mobilepay.html')

def banktransfer(request):
    return render(request,'facepay/banktransfer.html')

def recharge(request):
    return render(request,'facepay/recharge.html')

    
def facedetect(request):

    cam = cv2.VideoCapture(20)
    cam.open(0, cv2.CAP_DSHOW)
    s, img = cam.read()
    if s:
        face_1_image = face_recognition.load_image_file("faces//me.jpeg")
        face_1_face_encoding = face_recognition.face_encodings(face_1_image)[0]
        
        face_2_face_encoding = face_recognition.face_encodings(img)[0]
        
        check=face_recognition.compare_faces([face_1_face_encoding], face_2_face_encoding)
        print(check)
        if check[0]:
            messages.success(request, f'face successfully verified !')
            return redirect('payment')
    return render(request,'facepay/facedetect.html')  
    
def payment(request):
    return render(request,'facepay/payment.html')
def success(request):
    return render(request,'facepay/success.html')
def webcam(request):
    return render(request,'facepay/webcam.html')
