from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Guest,Movie,Reservation
# Create your views here.

#1 without Rest and no model query FBV
def no_rest_no_model(request):
    guests=[
        {
            'id':1,
            'name':'John',
            'mobile':"12555558"
        },
        {
            'id':2,
            'name':'David',
            'mobile':"87855558"
        },
    ]
    return JsonResponse(guests, safe=False)

#2 model data default django without rest
def  no_rest_with_model(request):
    data=Guest.objects.all()
    response={
        'guests':list(data.values('name','mobile'))
    }
    return JsonResponse(response)

#