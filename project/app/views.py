from django.shortcuts import render,redirect
from .models import *
from .forms import CustomerForm
from django.core.paginator import Paginator
from .filters import CustomerFilter
from django.contrib import messages
from django.db.models import Q

#--------------Index page-----------
def home(request):
	users_list=Customer.objects.all()
	return render(request, 'app/index.html', {'users':users_list})


#-----------Add User-----------
def add(request):
	if request.method == 'POST':
		print("add method")
		name=request.POST['name']
		pan=request.POST['pan']
		age=request.POST['age']
		
		email=request.POST['email']
		gender=request.POST['gender']
		city=request.POST['city']
		print(name, pan, age, gender, email, city)
		user=Customer.objects.create(name=name, pan=pan, age=age, gender=gender, email=email, city=city)
		user.save()
		messages.success(request, 'User is created')
		print("User is created")
		users_list=Customer.objects.all()
		return render(request, 'app/index.html', {'users':users_list})
						
	return render(request, 'app/add_user.html')

def deleteUser(request, pk):

	user=Customer.objects.get(id=pk)	
	
	if request.method == 'POST':
		user.delete()
		return redirect('/')
	context={'user':user}
	return render(request, 'app/delete_user.html', context)

def updateUser(request, pk):

	user=Customer.objects.get(id=pk)	
	form=CustomerForm(instance=user)
	if request.method == 'POST':
		form=CustomerForm(request.POST, instance=user)
		if form.is_valid():
			form.save()
			return redirect('/')
	context={'form':form, 'user':user}
	return render(request, 'app/update_user.html', context)

