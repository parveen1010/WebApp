from django.shortcuts import render,redirect
from .models import *
from .forms import CustomerForm
from django.core.paginator import Paginator
from .filters import CustomerFilter
from django.contrib import messages
from django.db.models import Q
import re
# Create your views here.

def checkEmail(email):	
	email_reg=re.search(r'\w+@[a-zA-Z]+\.[a-z]+\b', email)
	if email_reg!=None and email_reg.group(0)==email:
		match=Customer.objects.filter(Q(email__icontains=email))
		if match.first()==None:
			print('Pass Filter')
			return True
	else:
		return False
			

def checkName(name):
	name_reg=re.search(r'^\D+\b',name)
	if name_reg!=None and name_reg.group(0)==name:
		return True
	else:
		return False
def checkPan(pan):
	pan_reg=re.search(r'^[a-zA-Z0-9]+\b', pan)
	if pan_reg!=None and pan_reg.group(0)==pan:
		match=Customer.objects.filter(Q(pan__icontains=pan)) 
		if match.first()==None:
			return True
	else:
		return False


def home(request):
	if request.method == 'POST':
		sort=request.POST['sort']
		if sort=='Name':
			users_list=Customer.objects.order_by('name')
		elif sort=='PAN Number':
			users_list=Customer.objects.order_by('pan')
		elif sort=="City":
			users_list=Customer.objects.order_by('city')

		else:
			users_list=Customer.objects.all()
	else:
		users_list=Customer.objects.all()
	paginator=Paginator(users_list,10)
	try:
		page=request.GET.get('page', '1')
	except:
		page=1
	try:
		posts=paginator.page(page)
	except(EmptyPage, InvalidPage):
		posts=pagination.page(pagination.num_pages)
	return render(request, 'app/index.html', {'users':users_list, 'posts':posts})

def add(request):
	if request.method == 'POST':
		print("add method")
		name=request.POST['name']
		pan=request.POST['pan']
		age=request.POST['age']
		
		email=request.POST['email']
		gender=request.POST['gender']
		city=request.POST['city']
		if age=='':
			messages.error(request,"Age field can't be empty")
			return render(request, 'app/add_user.html')
		elif city=='':	
			messages.error(request,"Please select a city from drop down")
			return render(request, 'app/add_user.html')
		elif gender=='':
			messages.error(request,"Gender Field is empty")
			return render(request, 'app/add_user.html')
		else:
			age1=int(age)
			if checkName(name)==True:
				if checkEmail(email)==True:
						if checkPan(pan)==True:
							if age1>=1 and age1<=100:

								user=Customer.objects.create(name=name, pan=pan, age=age, gender=gender, email=email, city=city)
								user.save()
								messages.success(request, 'User is created')
								print("User is created")
								return render(request, 'app/add_user.html')
							else:
								messages.error(request, 'Age is invalid')
								return render(request, 'app/add_user.html')
						else:
							print('PAN Field')
							messages.error(request, 'PAN Number is invalid or not unique')
							return render(request, 'app/add_user.html')
				else:
					print('Email field')
					messages.error(request, 'Email is invalid or not unique')
					return render(request, 'app/add_user.html')
			else:
				messages.error(request, 'Name is invalid')
				return render(request, 'app/add_user.html')
	else:
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


def searchUser(request):
	if request.method=='POST':
		srch=request.POST['name']
		if srch!='':
			match=Customer.objects.filter(Q(name__icontains=srch) | Q(city__icontains=srch) |Q(pan__icontains=srch))
			if match:
				messages.success(request, 'Found Result')
				return render(request, 'app/search.html', {'customer':match})

			else:
				messages.error(request, 'No result found')
				return render(request, 'app/search.html')
		
		else:
			return render(request, 'app/search.html')
	else:
		context={}		
		return render(request, 'app/search.html', context)

