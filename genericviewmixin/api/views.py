# GenericAPIView and Model Mixin
from .models import Student
from .serializers import StudentSerializers
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

# List and Create - PK not required
class LCStudentAPI(GenericAPIView,ListModelMixin,CreateModelMixin):
	queryset = Student.objects.all()
	serializer_class = StudentSerializers

	def get(self,request,*args,**kwargs):
		return self.list(request,*args,**kwargs)

	def post(self,request,*args,**kwargs):
		return self.create(request,*args,**kwargs)

# Retrive Update and Destroy - PK is Required
class RUDStudentAPI(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
	queryset = Student.objects.all()
	serializer_class = StudentSerializers

	def get(self,request,*args,**kwargs):
		return self.retrieve(request,*args,**kwargs)

	def put(self,request,*args,**kwargs):
		return self.update(request,*args,**kwargs)

	def delete(self,request,*args,**kwargs):
		return self.destroy(request,*args,**kwargs)



# class StudentList(GenericAPIView,ListModelMixin):
# 	queryset = Student.objects.all()
# 	serializer_class = StudentSerializers
# 	def get(self,request,*args,**kwargs):
# 		return self.list(request,*args,**kwargs)

# class StudentCreate(GenericAPIView,CreateModelMixin):
# 	queryset = Student.objects.all()
# 	serializer_class = StudentSerializers
# 	def post(self,request,*args,**kwargs):
# 		return self.create(request,*args,**kwargs)


# class StudentRetrieve(GenericAPIView,RetrieveModelMixin):
# 	queryset = Student.objects.all()
# 	serializer_class = StudentSerializers
# 	def get(self,request,*args,**kwargs):
# 		return self.retrieve(request,*args,**kwargs)

# class StudentUpdate(GenericAPIView,UpdateModelMixin):
# 	queryset = Student.objects.all()
# 	serializer_class = StudentSerializers
# 	def put(self,request,*args,**kwargs):
# 		return self.update(request,*args,**kwargs)

# class StudentDelete(GenericAPIView,DestroyModelMixin):
# 	queryset = Student.objects.all()
# 	serializer_class = StudentSerializers
# 	def delete(self,request,*args,**kwargs):
# 		return self.destroy(request,*args,**kwargs)




