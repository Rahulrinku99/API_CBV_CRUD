from django.shortcuts import render
from app.models import *
from app.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@permission_classes([IsAuthenticated])
class ProductDetails(APIView):
    def get(self,request,Pid):
        PQS=Product.objects.all()
        PJD=ProductMS(PQS,many=True)
        return Response(PJD.data)
    

    def post(self,request,Pid):
        PMSD=ProductMS(data=request.data)
        if PMSD.is_valid():
            spo=PMSD.save()
            return Response({'message':'Product is created'})
        else:
            return Response({'failed':''})
        
    def put(self,request,Pid):
        Pid=request.data['Pid']
        productobject=Product.objects.get(Pid=Pid)
        PMSD=ProductMS(productobject,data=request.data)
        if PMSD.is_valid():
            PMSD.save()
            return Response({'Message':'Product is updated'})
        return Response({'failed':'Product is not updated'})
    
    def patch(self,request):
        Pid=request.data['Pid']
        PO=Product.objects.get(Pid=Pid)
        PO.Pname=request.data['Pname']
        PO.save()
        return Response({'success':'Data is Partially Updated'})

    def delete(self,request,Pid):
        Product.objects.get(Pid=Pid).delete()
        return Response({'success':'Product is deleted'})
    