from django.shortcuts import render
from .serializers import StudentSerializers
from .models import Student
from rest_framework.generics import ListAPIView
# from .pagination import MypageNumber
# from .pagination import Myofsetpagination
from .pagination import MyCursorPagination


# class StudentList(ListAPIView):
# 	queryset = Student.objects.all()
# 	serializer_class = StudentSerializers
# 	pagination_class = MypageNumber


# class StudentList(ListAPIView):
# 	queryset = Student.objects.all()
# 	serializer_class = StudentSerializers
# 	pagination_class = Myofsetpagination


class StudentList(ListAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializers
	pagination_class = MyCursorPagination
