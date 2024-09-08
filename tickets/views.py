from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Guest,Movie,Reservation
from rest_framework.decorators import api_view
from .serializers import GuestSerializer,ReservationSerializer,MovieSerializer
from  rest_framework import status,filters
from  rest_framework.response import Response


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

#3 function based views
#3.1 GET POST
@api_view(['GET','POST'])
def FBV_List(request):
    #GET
    if request.method == 'GET':
        guests=Guest.objects.all()
        serializer=GuestSerializer(guests, many=True)
        return Response(serializer.data)
    #POST
    elif request.method=='POST':
        serializer=GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)





#3.2 GET PUT DELETE
# @api_view()
# def