from rest_framework import serializers
from .models import Student


class StudentsSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Student
		fields = ['id','url','name','roll','city']