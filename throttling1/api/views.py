from .models import Student
from .serializers import StudentSerializers
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,
UpdateAPIView,DestroyAPIView
from rest_framework.throttling import ScopedRateThrottle

class StudentList(ListAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializers
	throttling_classes = [ScopedRateThrottle]
	throttle_scope = 'viewstu'

class StudentCreate(CreateAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializers
	throttling_classes = [ScopedRateThrottle]
	throttle_scope = 'modifystu'

class StudentRetrieve(RetrieveAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializers
	throttling_classes = [ScopedRateThrottle]
	throttle_scope = 'viewstu'

class StudentUpdate(UpdateAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializers
	throttling_classes = [ScopedRateThrottle]
	throttle_scope = 'modifystu'

class StudentDelete(DestroyAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializers
	throttling_classes = [ScopedRateThrottle]
	throttle_scope = 'modifystu'


