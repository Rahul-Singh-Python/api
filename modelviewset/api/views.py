from .models import Student
from .serializers import StudentSerializers
from rest_framework import viewsets

# # Read and Retrieve
class StudentReadOnlyModel(viewsets.ReadOnlyModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializers






# # READ,CREATE,RETRIVE,UPDATE,DELETE
# class StudentModelViewSet(viewsets.ModelViewSet):
# 	queryset = Student.objects.all()
# 	serializer_class = StudentSerializers

