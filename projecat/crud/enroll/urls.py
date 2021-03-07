from django.urls import path,include
from . import views

urlpatterns=[
	path('',views.add_show,name='addandshow'),
	path('<int:id>/',views.update_data,name='updatedata'),
	path('delete/<int:id>/',views.deletedata,name='deletedata'),
	path('<int:id>/',views.update_data,name='updatedata'),
	path('api/',include('enroll.api.urls')),
]