
from django.shortcuts import render
from django.http.response import JsonResponse 
from .models import *
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework import status,filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics,mixins,viewsets

# Create your views here.
#----------------------------------------------------------------------------------------------------
#1
# //no rest and no model

def no(request):
    guests=[
        {
            "id" : 1,
            "name" : "mo",
            "mobile" : 123,
        },
        {
            "id" : 2,
            "name" : "moh",
            "mobile" : 1234,
        }
    ]
    return JsonResponse (guests , safe=False)
#----------------------------------------------------------------------------------------------------
#2
# model data default django with out rest  //no rest with model
def no1(request):
    data = Guest.objects.all()
    responce ={
        'guests' : list(data.values('name','mobile'))  
    }
    return JsonResponse(responce)
#----------------------------------------------------------------------------------------------------   
# 3
# List == GET
# Create == POST

# PK Query == GET
# Update == PUT
# Delete / Destroy == DELETE 

# Function Based Views
# 3.1 GET , POST
@api_view(['GET','POST'])
def FBV_List(request):
    # GET
    if request.method == 'GET':
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many= True)
        return Response(serializer.data)
    
    # POST
    elif request.method == 'POST':
        serializer = GuestSerializer(data=request.data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data , status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.data , status=status.HTTP_400_BAD_REQUEST)


# 3.2 GET , PUT , DELETE
@api_view(['GET','PUT','DELETE'])
def FBV_pk(request,pk):
    try :
        guest = Guest.objects.get(pk=pk)
    except Guest.DoesNotExist :
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        serializer = GuestSerializer(guest)
        return Response(serializer.data)
    
    # PUT
    elif request.method == 'PUT':
        serializer = GuestSerializer(guest,data=request.data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        
    # DELETE
    elif request.method == 'DELETE':
        serializer = guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(serializer.data , status=status.HTTP_400_BAD_REQUEST)
    
#----------------------------------------------------------------------------------------------------
# 4
# CBV Class based views
# 4.1
# List And Create == GET & POST
class CBV_list(APIView):
    def get(self, request):
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many= True)
        return Response(serializer.data)
    def post(self, request):
        serializer = GuestSerializer(data=request.data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data , status=status.HTTP_400_BAD_REQUEST)
        
# 4.2 
# GET , PUT , DELETE
class CBV_pk(APIView):
    #main
    def get_object(self, pk):
        try:
            return Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            raise Http404
    #GET 
    def get(self, request, pk):
        guest = self.get_object(pk)
        serializer = GuestSerializer(guest)
        return Response(serializer.data)
    #PUT 
    def put(self, request, pk):
        guest = self.get_object(pk)
        serializer = GuestSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #DELETE 
    def delete(self, request, pk):
        guest = self.get_object(pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#----------------------------------------------------------------------------------------------------
# 5
# mixins
# 5.1
# mixins list
class Mixins_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset= Guest.objects.all()
    serializer_class=GuestSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
    
# 5.2
class Mixins_pk(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset= Guest.objects.all()
    serializer_class=GuestSerializer
    def get(self,request,pk):
        return self.retrieve(request,pk)
    def put(self,request,pk):
        return self.update(request,pk)
    def delete(self,request,pk):
        return self.destroy(request,pk)
#----------------------------------------------------------------------------------------------------
# 6
# Generics
# 6.1 
# GET & POST
class generics_list(generics.ListCreateAPIView):
    queryset= Guest.objects.all()
    serializer_class=GuestSerializer
# 6.2 
# GET & PUT & DELETE
class generics_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset= Guest.objects.all()
    serializer_class=GuestSerializer
#----------------------------------------------------------------------------------------------------
# 7
# viewsets // king of all
class viewsets_guest(viewsets.ModelViewSet):
    queryset= Guest.objects.all()
    serializer_class=GuestSerializer    

    
class movies(viewsets.ModelViewSet):
    queryset= Movie.objects.all()
    serializer_class=MovieSerializer   
    filter_backends=[filters.SearchFilter] 
    search_field = ['movie']

    
class resevation(viewsets.ModelViewSet):
    queryset= Resevation.objects.all()
    serializer_class=ResevationSerializer    
#----------------------------------------------------------------------------------------------------
# 8
# research movie

@api_view(['GET'])
def find_movie(request):
    movies=Movie.objects.filter(
        hall=request.data['hall'],
        movie=request.data['movie'],
    )
    serializer = MovieSerializer(movies,many = True)
    return Response(serializer.data)
#----------------------------------------------------------------------------------------------------

# 9 
# create new reservation
@api_view(['POST'])
def create_reservation(request):
    movies=Resevation.objects.filter(
        hall=request.data['hall'],
        movie=request.data['movie'],
        Resevation=request.data['Resevation']
    )
    serializer = MovieSerializer(movies,many = True)
    return Response(serializer.data)