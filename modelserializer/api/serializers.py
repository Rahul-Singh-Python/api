from rest_framework import serializers
from .models import Student

# class StudentSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Student
# 		fields = ['id','name','roll','city']





## Read_only  
# # one field 
# class StudentSerializer(serializers.ModelSerializer):
# 	name = serializers.CharField(read_only=True)
# 	class Meta:
# 		model = Student
# 		fields = ['name','roll','city']


# # Read_only  
# # multiple field 
# class StudentSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Student
# 		fields = ['name','roll','city']
# 		# read_only_fields = ['name','roll']
# 		extra_kwargs = {'name':{'read_only':True}}




class StudentSerializer(serializers.ModelSerializer):
	
	# Validators
	def start_with_r(value):
		if value[0].lower() != 'r':
			raise serializers.ValidationError("Name Should be start with R")
	name = serializers.CharField(validators=[start_with_r])

	class Meta:
		model = Student
		fields = ['name','roll','city']



	# Field Lavel Validation
	def validate_roll(self,value):
		if value >= 200:
			raise serializers.ValidationError('Seat Full')
		return value

	# Object Lavel Validation
	def validate(self,data):
		nm = data.get('name')
		ct = data.get('city')
		if nm.lower() == 'Rahul' and ct.lower() != 'Surat':
			raise serializers.ValidationError('City Must Be Surat')
		return data

	