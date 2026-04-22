from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Home Page Working</h1>")

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import student, college
from .serializers import studentserializer, collegeserializer

# GET + POST
@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET':
        student = student.objects.all()
        serializer = studentserializer(student, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


# GET ONE + PUT + DELETE
@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, id):
    student = student.objects.get(id=id)

    if request.method == 'GET':
        serializer = studentserializer(student)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = studentserializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        student.delete()
        return Response({"message": "Deleted"})

# Create the same for college

@api_view(['GET', 'POST'])
def college_list(request):
    if request.method == 'GET':
        college = college.objects.all()
        serializer = collegeserializer(college, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = collegeserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def college_detail(request, id):
    college = college.objects.get(id=id)

    if request.method == 'GET':
        serializer = collegeserializer(college)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = collegeserializer(college, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        college.delete()
        return Response({"message": "Deleted"})

from rest_framework.viewsets import ModelViewSet

class StudentViewSet(ModelViewSet):
    queryset = student.objects.all()
    serializer_class = studentserializer