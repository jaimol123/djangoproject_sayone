from django.shortcuts import render,redirect
from django.http import HttpResponse
import json
from .models import Images,Validation
from django.contrib.auth.models import User,Group 


def signup(request):
	return render(request,"signup.html")

def return1(request):
	return render(request,"user_login.html")
def success(request):
	return render(request,"success.html")
def failure(request):
	return render(request,"failure.html")
def userlogin(request):
	return render(request,"user_login.html")
def upload(request):
	return render(request,"post.html")
def viewpost(request):
	return render(request,"view_post.html")

def viewlike(request):
	return render(request,"view_like.html")

def signupfn(request):
	dict1={}
	try:
		firstname=request.POST['first']
		
		lastname=request.POST['last']
		username=request.POST['user']
		designation=request.POST['desig']
		password=request.POST['psd']
		confirm_password=request.POST['con']
		if(username!="" and password!="" and firstname!="" and lastname!=""):
			if(confirm_password==password):
				u1=User(first_name=firstname,last_name=lastname,username=username,password=password,is_superuser=0)
				u1.save()
				dict1["val"]=1
			else:
				dict1["val"]=2
		
			
		else:
			dict1["val"]=0
	except Exception as e:
		dict1["status"]=False
		print("exception in sifnupfn",e)
	jsondata=json.dumps(dict1)
	return HttpResponse(jsondata,content_type="application/json")
	

def userloginfn(request):
	dict6={}
	try:
		username=request.POST['users']
		request.session["user"]=username
		password=request.POST['psd1']
		request.session["pass"]=password
		print("password via post",password)
		u2=User.objects.get(username=username)
		user1=u2.username
		pass1=u2.password
		fname=u2.first_name
		request.session["fname1"]=fname
		
		if(username==user1 and password==pass1):
				dict6["val1"]=1
		if(password!=pass1):
				dict6["val2"]=0
		
	except Exception as e:
		
		print("exception in userloginfn",e)
		return render(request,"failure.html")
	jsondata=json.dumps(dict6)
	return HttpResponse(jsondata,content_type="application/json")




def uploadfn(request):
	dict55={}
	try:
		name=request.session["fname1"]
		text_msg=request.POST['text_name']
		print("text",text_msg)
		images=request.FILES['image']
		print("image output---------------->",images)	
		
		if(text_msg!="" and name!=""):
			i1=Images(name2=name,text1=text_msg,image=images,status=0)
			i1.save()
			dict55["status"]=True
		
		
	except Exception as e:
		dict55["status"]=False
		print("exception in uploadfn",e)
		return render(request,"failure.html")
	jsondata=json.dumps(dict55)
	return HttpResponse(jsondata,content_type="application/json")



def viewpostfn(request):
		dict3={}
		res=""
		try:
			i2=Images.objects.all()
			for x in i2:
				res += x.name2+"  "+"updated her post"+"\n"+"->>>"+x.text1+"\n"+"\n"
				dict3["val1"]=res
			dict3["status"]=True
		except Exception as e:
			dict3["status"]=False
			print("exception in viewpostfn",e)
		jsondata=json.dumps(dict3)
		return HttpResponse(jsondata,content_type="application/json")
		

def likefn(request):
	lis1=[]
	dict4={}
	res=""
	try:
		like_name=request.POST['liked']
		
		user1=request.session["user"]
		pass1=request.session["pass"]
		
		
		
		try:
			v1=Validation.objects.get(username1=user1,password1=pass1,likedname=like_name)
			
		except Exception as e:
			v1=None
			print("except inside except",e)
		if(v1==None):
			
			i4=Images.objects.get(name2=like_name)
			stat=i4.status
			stat=stat+1
			i4.status=stat
			i4.save()
			i5=Validation(username1=user1,password1=pass1,likedname=like_name)
			i5.save()
			dict4["yes"]=5
			
			i9=Images.objects.filter(name2=like_name)
			for x in i9:
				lis1.append(x.text1)
			print("list in likefn------------->",lis1)
			dict4["lis"]=lis1
			
					
		if(v1!=None):
			dict4["no"]=4	
		

			
	except Exception as e:
		print("exception in likefn",e)
		dict4["status"]=False
	jsondata=json.dumps(dict4)
	return HttpResponse(jsondata,content_type="application/json")



def viewlikefn(request):
		dict11={}
		try:
			l_name=request.POST['lname']
			r=Images.objects.get(name2=l_name)
			stat1=r.status
			dict11["val1"]=stat1
			dict11["status"]=True
		except Exception as e:
			print("exception in viewlikefn",e)
			dict11["status"]=False
		jsondata=json.dumps(dict11)
		return HttpResponse(jsondata,content_type="application/json")










