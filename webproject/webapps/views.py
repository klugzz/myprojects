from django.shortcuts import render,redirect
from webapps.models import Student
from webapps.forms import StudentForm
def read(request):
	student=Student.objects.all()
	return render (request,'apps/result/html',{'e':student})
def insert(request):
	form=StudentForm()
	if request.method=="POST":
		form=StudentForm(request.POST)
		if form.is_valid():
			form.save()
	return render(request,'apps/insert.html',{'form':form})
def delete(request):
	e=Student.objects.get(id=id)
	e.delete()
	return redirect('/result')
def update(request,id):
	student=Student.objects.get(id=id)
	if request.method=="POST":
		form=StudentForm(request.POST,instances=student)
		if form.is_valid():
			form.save()
		return redirect('/result')
	return render(request,'apps/update.html',{'e':student})

def delete(request,id):
	e=Student.objects.get(id=id)
	e.delete()
	return redirect('/result')
def update(request):
	student=Student.objects.get(id=id)
	if request.method=="POST":
		form=StudentForm(request.POST,instance=student)
		if form.is_valid():
			form.save()
		return redirect('/result')
	return render(request,'apps/update.html',{'e':student})

def index(request):
	return render(request,'apps/index.html')
def home(request):
	return render(request,'apps/home.html')
def service(request):
	return render(request,'apps/services.html')
def gallery(request):
	return render (request,'apps/gallery.html')
def contact(request):
	return render (request,'apps/contact.html')