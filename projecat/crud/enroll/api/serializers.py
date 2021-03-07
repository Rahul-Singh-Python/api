from rest_framework import serializers
from enroll.models import user


class UserSerializers(serializers.ModelSerializer):
	class Meta:
		model = user
		fields = ['id','name','email','password']