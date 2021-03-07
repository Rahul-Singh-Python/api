from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializers
from rest_framework import status
from rest_framework import viewsets

class StudentViewSet(viewsets.ViewSet):
	def list(self,request):
		print("*************LIST*****************")
		print("Basename",self.basename)
		print("Action",self.action)
		print("Detail",self.detail)
		print("Suffix",self.suffix)
		print("Name",self.name)
		print("Description",self.description)
		stu = Student.objects.all()
		serializer = StudentSerializers(stu,many=True)
		return Response(serializer.data)

	def retrieve(self,request,pk=None):
		print("*************RETRIEVE*****************")
		print("Basename",self.basename)
		print("Action",self.action)
		print("Detail",self.detail)
		print("Suffix",self.suffix)
		print("Name",self.name)
		print("Description",self.description)
		id = pk
		if id is not None:
			stu = Student.objects.get(id=id)
			serializer = StudentSerializers(stu)
			return Response(serializer.data)

	def create(self,request):
		print("*************CREATE*****************")
		print("Basename",self.basename)
		print("Action",self.action)
		print("Detail",self.detail)
		print("Suffix",self.suffix)
		print("Name",self.name)
		print("Description",self.description)
		serializer = StudentSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	def update(self,request,pk):
		print("*************UPDATE*****************")
		print("Basename",self.basename)
		print("Action",self.action)
		print("Detail",self.detail)
		print("Suffix",self.suffix)
		print("Name",self.name)
		print("Description",self.description)
		id = pk
		stu = Student.objects.get(pk=id)
		serializer = StudentSerializers(stu,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'Complete Data Updated'},status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	def partial_update(self,request,pk):
		print("*************PARTIAL UPDATE*****************")
		print("Basename",self.basename)
		print("Action",self.action)
		print("Detail",self.detail)
		print("Suffix",self.suffix)
		print("Name",self.name)
		print("Description",self.description)
		id = pk
		stu = Student.objects.get(pk=id)
		serializer = StudentSerializers(stu,data=request.data,partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'Partial Data Updated'})
		return Response(serializer.errors)


	def delete(self,request,pk):
		print("*************DELETE*****************")
		print("Basename",self.basename)
		print("Action",self.action)
		print("Detail",self.detail)
		print("Suffix",self.suffix)
		print("Name",self.name)
		print("Description",self.description)
		id = pk
		stu = Student.objects.get(pk=id)
		stu.delete()
		return Response({'msg':'Data Deleted'})
