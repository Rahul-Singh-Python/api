from django.shortcuts import render
from .serializers import StudentsSerializers
from .models import Student
from rest_framework import viewsets


class StudentModelViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentsSerializers