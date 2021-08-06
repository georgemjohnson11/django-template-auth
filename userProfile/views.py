from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import UserProfile
from .serializers import *

from django.shortcuts import render

def index(request):
    return render(request, './google-auth-page.html')

@api_view(['GET', 'POST'])
def userProfile_list(request):
    if request.method == 'GET':
        data = UserProfile.objects.all()

        serializer = UserProfileSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def userProfiles_detail(request, pk):
    try:
        userProfile = UserProfile.objects.get(pk=pk)
    except UserProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = UserProfileSerializer(userProfile, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)