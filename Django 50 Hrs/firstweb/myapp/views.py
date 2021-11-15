from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
#from django.http import HttpResponse โชข้อความหน้าเว็บ
 
def Home(request):
	product1 = 'register'
	product2 = 'Booking'
	product3 = 'AboutUs' 

	context = {'product1':product1,'product2':product2,'product3':product3}
	return render(request,'myapp/home.html',context)
def login(request):
	return render(request,'myapp/login.html')

from django.contrib.auth.models import User

def Register(request):
	if request.method == 'POST':
		data = request.POST.copy()
		first_name = data.get('first_name')
		last_name = data.get('last_name')
		email = data.get('email')
		password = data.get('password')
		newuser = User()
		newuser.username = email
		newuser.email =email
		newuser.last_name = last_name
		newuser.set_password()
		newuser.save()
	return render(request,'myapp/register.html')

def About(request):
	return render(request,'myapp/about.html')

def Contact(request):
	return render(request,'myapp/contact.html')	

def Flightstatus(request):
	return render(request,'myapp/flightstatus.html')	


	#return HttpResponse('<h1>สวัสดีวันนี้เรามาพบกัน</h1>')

