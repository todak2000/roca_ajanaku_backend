from django.shortcuts import render
import datetime
import json
import requests
import jwt
from django.core.files.storage import FileSystemStorage
from server.models import (JoinUs)
from CustomCode import (autentication, fixed_var, password_functions,
                        string_generator, validator, send_email)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from roca import settings
from django.core.mail import EmailMessage
from django.core.files.storage import FileSystemStorage
# Create your views here.
# REST_API_ID = 'b3776bdc121a923ba560cac5036076b4'
# REST_API_SECRET = '8ed97a421c3954ef64a29cbd2dd85d65'
# TOKEN_STORAGE = 'memcached'
# MEMCACHED_HOST = '127.0.0.1:11211'
# SPApiProxy = PySendPulse(REST_API_ID, REST_API_SECRET, TOKEN_STORAGE, memcached_host=MEMCACHED_HOST)
@api_view(['GET'])
def index_page(request):
    return_data = {
        "error" : "0",
        "status" : 200,
        "message" : "Successful"
    }
    return Response(return_data)

# JOIN US API
@api_view(["POST"])
def join_us(request):
    try:
        name = request.data.get('name',None)
        phoneNumber = request.data.get('phonenumber',None)
        email = request.data.get('email',None)
        resumelink= request.data.get('resumelink',None)

        field = [name,phoneNumber,email, resumelink]
        if not None in field and not "" in field:
            try:
                # fs = FileSystemStorage()
                # filename = fs.save(document.name, document)
                # uploaded_file_url = fs.url(filename)
                n = JoinUs(name=name, email=email, phone=phoneNumber, document=resumelink)
                n.save()
                subject = name+' Would like to Join Roca & Ajanaku'
                message = "I, " +name+" would like to join Roca & Ajanaku. Please, kindly reach me on "+phoneNumber+" or "+email+". Attached is my Resume: "+resumelink+" and I look forward to hearing from you. Thanks. Download here: "
                send_email.send_email(subject,email,message)
                return_data = {
                    "error": "0",
                    "message": name+", your Resume has beed delivered. We will get in touch with you as soon as possible. Thank you"
                }
            except Exception as e:
                return_data = {
                    "error": "31",
                    "message": str(e)
                }
        else:
            return_data = {
                "error":"2",
                "message": "One or more fields is empty!"
            }
    except Exception as e:
        return_data = {
            "error": "3",
            "message": str(e)
        }
    return Response(return_data)