from django.shortcuts import render
import datetime
import json
import requests
import jwt
from django.core.files.storage import FileSystemStorage
from server.models import (JoinUs)
from CustomCode import (autentication, fixed_var, password_functions,
                        string_generator, validator)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from roca import settings
from django.core.mail import EmailMessage

# Create your views here.

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
        document = request.FILES.getlist('attach')
        field = [name,phoneNumber,email]
        if not None in field and not "" in field:
            subject = name+' Would like to Join Roca & Ajanaku'
            message = "I, " +name+" would like to join Roca & Ajanaku. Please, kindly reach me on "+phoneNumber+" or "+email+". Attached is my Resume and I look forward to hearing from you. Thanks."
            to_email = "todak2000@gmail.com"
            from_email = "WasteCoin"

            try:
                email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, to=[to_email])
                for f in document:
                        email.attach(f.name, f.read(), f.content_type)
                email.send()
                return_data = {
                    "error": "0",
                    "message": name+", your Resume has beed delivered. We will get in touch with you as soon as possible. Thank you"
                }
            except Exception as e:
                return_data = {
                    "error": "3",
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