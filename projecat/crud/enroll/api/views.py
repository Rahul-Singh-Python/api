from enroll.models import user
from enroll.api.serializers import UserSerializers
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class UserViewSet(viewsets.ModelViewSet):
	queryset = user.objects.all()
	serializer_class = UserSerializers
	authentication_classes = [SessionAuthentication]
	permission_classes = [IsAuthenticatedOrReadOnly]