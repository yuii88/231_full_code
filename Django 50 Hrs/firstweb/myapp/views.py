from django.shortcuts import render
from django.http import HttpResponse
#from django.http import HttpResponse โชข้อความหน้าเว็บ
 
def Home(request):
	product1 = 'register'
	product2 = 'Booking'
	product3 = 'AboutUs'

	context = {'product1':product1,'product2':product2,'product3':product3}
	return render(request,'myapp/home.html',context)

def About(request):
	return render(request,'myapp/about.html')

def Contact(request):
	return render(request,'myapp/contact.html')	

def Flightstatus(request):
	return render(request,'myapp/flightstatus.html')	


	#return HttpResponse('<h1>สวัสดีวันนี้เรามาพบกัน</h1>')

