from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework import Response, request, status
# Create your views here.
from .serializer import *

class  ProductViewset(APIView):
    
    
    def get(self, request):
        if request.GET.get('type') == 'Laptop':
            data=ProductDetails.objects.filter(product__type=request.GET.get('type'))
            serilizer=MobiletSerializer(data=data)
            return Response(serilizer)
        
        elif request.GET.get('type') == 'Mobile':
            data=ProductDetails.objects.filter(product__type=request.GET.get('type'))
            serilizer=LaptopSerializer(data=data)
            return Response(serilizer)
    
    
    def post(self,Request):
        if request.POST.post('type') == 'Laptop':
            data=ProductDetails.objects.filter(product__type=request.POST.post('type'))
            serilizer=ProductSerializer(data=data)
            return Response(serilizer)
        
    def Put(self, request,pk):
        snippet = self.get_object(pk)
        serializer = ProductSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
                
