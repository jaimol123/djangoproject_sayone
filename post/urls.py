from django.urls import path
from . import views
import django.conf.urls 
import django.views.generic 

urlpatterns=[
	path('',views.userlogin,name="userlogin"),
	path('userloginfn',views.userloginfn,name="userloginfn"),
	path('signup',views.signup,name="signup"),
	path('signupfn',views.signupfn,name="signupfn"),
	path('success',views.success,name="success"),
	path('failure',views.failure,name="failure"),
	path('upload',views.upload,name="upload"),
	path('uploadfn',views.uploadfn,name="uploadfn"),
	path('viewpost',views.viewpost,name="viewpost"),
	path('viewpostfn',views.viewpostfn,name="viewpostfn"),
	path('likefn',views.likefn,name="likefn"),
	path('viewlike',views.viewlike,name="viewlike"),
	path('viewlikefn',views.viewlikefn,name="viewlikefn"),
	path('return1',views.return1,name="return1"),

	
	
		

]
