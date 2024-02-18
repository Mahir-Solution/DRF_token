from django.shortcuts import render
from rest_framework.views import APIView
from .models import Chair
from .serializer import ChairSerializer
from rest_framework.response import Response
from rest_framework import status

class ChairAPI(APIView):
    def get(self,request, pk= None, format = None):
        id = pk
        if id is not None:
            chair_data = Chair.objects.get(id = id)
            seri_data = ChairSerializer(chair_data)
            return Response(seri_data.data)
        
        else:
            chair_data = Chair.objects.all()
            seri_data = ChairSerializer(chair_data, many = True)
            return Response(seri_data.data)
        
    
    def put(self,request,pk,format = None):
        id = pk
        old_data = Chair.objects.get(id = id)
        seri_data = ChairSerializer(old_data,data=request.data)
        if seri_data.is_valid():
            seri_data.save()
            return Response({'update msg': "data has been update succesfully"})
        else:
            return Response(seri_data.errors)
        
    
    def patch(self,request,pk,format = None):
        id = pk
        old_data = Chair.objects.get(id = id)
        seri_data = ChairSerializer(old_data,data=request.data, partial = True)
        if seri_data.is_valid():
            seri_data.save()
            return Response({'update msg': "data has been update succesfully"})
        else:
            return Response(seri_data.errors)
        
    def post(self,request, format = None ):
        data = request.data
        seri_data = ChairSerializer(data=data)
        if seri_data.is_valid():
            seri_data.save()
            return Response({'msg':'data is inserted successfully'},status= status.HTTP_201_CREATED)
        else:
            return Response(seri_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk,format=None):
        id = pk
        if id is not None:
            fetch_data = Chair.objects.get(id = id)
            fetch_data.delete()
            return Response({'msg':'data delete successfully'})
        
        
            

# Create your views here.
