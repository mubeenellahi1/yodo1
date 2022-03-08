from django.shortcuts import render,redirect
from geodata.serializers import GeoDataSerializer
from .models import GeoData
from rest_framework.decorators import api_view
from rest_framework.response import Response



def geodata_list_view(request):
    unapproved = GeoData.objects.filter(approved=False)
    approved = GeoData.objects.filter(approved=True)
    return render(request,'./list.html',{'unapproved':unapproved,"approved":approved})

def geodata_approve_view(request,id):
    geodata = GeoData.objects.get(pk=id)
    geodata.approved = True
    geodata.save()
    return redirect('geodata_list_view')


@api_view(['POST'])
def geodata_create_apiview(request):
    serializer = GeoDataSerializer(data=request.POST)

    if serializer.is_valid(raise_exception=True):
        serializer.save()
   
    return Response({"message": "Data Saved"})

