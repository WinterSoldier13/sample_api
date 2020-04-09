from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
import firebase.firebase as fire
import pyrebase


# Create your views here.

@api_view(["GET"])


def test(request, details):
    details = str(details)
    details.replace('%20',' ')
    details.replace('%22',' ')
    details = details.strip()
    print(details)
    f= open('/home/wintersoldier/Desktop/aaaa.txt','w')
    f.write(details)
    f.close()
    return JsonResponse(str(details),safe=False)

def add_user(email,name,phone):
    try:
        firebase = fire.FirebaseApplication('https://api-test-c209a.firebaseio.com/')
    
        data ={'Name':name,
                'email':email,
                'phone':phone,
                }
        key = firebase.post('/api-test-c209a/customer_data',data)

        key=str(key)

        return JsonResponse("key: "+key,safe=False)



    except ValueError as e:
        return Response(e.args[0],status=status.HTTP_400_BAD_REQUEST)

def get_user_data(key):
    try:
        firebase = fire.FirebaseApplication('https://api-test-c209a.firebaseio.com/')
        result = firebase.get('/api-test-c209a/customer_data', key)

        return JsonResponse(str(result),safe=False)

    except ValueError as e:
        return Response(e.args[0],status=status.HTTP_400_BAD_REQUEST)


def signup_user(request,details):
    # details = "Ayush Singh,ayushsingh1315@gmail.com,password,phone"
    details = str(details)
    details.replace('%20',' ')
    details.replace('%22',' ')
    details = details.strip()
    name,email,password,phone = details.split(',')
    firebase_config = {
    'apiKey': "AIzaSyC81ny2CZ-baIACUOcIrjw_JTwbhQmxlds",
    'authDomain': "api-test-c209a.firebaseapp.com",
    'databaseURL': "https://api-test-c209a.firebaseio.com",
    'projectId': "api-test-c209a",
    'storageBucket': "api-test-c209a.appspot.com",
    'messagingSenderId': "95015707773",
    'appId': "1:95015707773:web:0e42cec09fa6419e0e3d14",
    'measurementId': "G-D8MSHXW66X"
    }
    firebase = pyrebase.initialize_app(firebase_config)

    auth = firebase.auth()
    try:
        user = auth.create_user_with_email_and_password(email,password)
        firebase = fire.FirebaseApplication('https://api-test-c209a.firebaseio.com/')
    
        data ={'Name':name,
                'email':email,
                'phone':phone,
                }
        key = firebase.post('/api-test-c209a/customer_data',data)

        key=str(key)

        return JsonResponse("key: "+key,safe=False)
    except:
        return JsonResponse("ERROR: User Already Exists",safe=False)
    add_user(email,name,phone)


def login_user(request,details):
    # details = "ayushsingh1315@gmail.com,password"
    details = str(details)
    details.replace('%20',' ')
    details.replace('%22',' ')
    details = details.strip()
    email,password = details.split(',')
    firebase_config = {
    'apiKey': "AIzaSyC81ny2CZ-baIACUOcIrjw_JTwbhQmxlds",
    'authDomain': "api-test-c209a.firebaseapp.com",
    'databaseURL': "https://api-test-c209a.firebaseio.com",
    'projectId': "api-test-c209a",
    'storageBucket': "api-test-c209a.appspot.com",
    'messagingSenderId': "95015707773",
    'appId': "1:95015707773:web:0e42cec09fa6419e0e3d14",
    'measurementId': "G-D8MSHXW66X"
    }
    firebase = pyrebase.initialize_app(firebase_config)

    auth = firebase.auth()
    try:
        login = auth.sign_in_with_email_and_password(email,password)
        return JsonResponse("login_successful",safe=False)
    except:
        return JsonResponse("ERROR: Please check your password",safe=False)

    








