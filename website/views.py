#from nis import cat
from multiprocessing import context
from unicodedata import name
from urllib.request import Request
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from pymysql import install_as_MySQLdb 
from .models import *
from .forms import *
from urllib.parse import urlencode
from django.contrib import messages
from django.contrib import auth

from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.forms import AuthenticationForm

##############################################################

def home(request): 
    slider = systemImageBilgi.objects.all()
    context = {}
    return render(request,"front_end/home/index.html",context)

def detay_kisi_create(request):
    form = DetayCreate()
    if request.method == 'POST':
        Url=request.POST['url']
        name=request.POST['name']
        surname=request.POST['surname']
        phone_number = request.POST['phone_number']
        birth_date = request.POST['birth_date']
        city = request.POST['city']
        KisiDetay.objects.create(name=name,surname=surname,birth_date=birth_date,phone_number=phone_number,url=Url,city=city)

        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER'))
    getKisi = KisiDetay.objects.all()
    context = {'form':form, 'KisiDetay':getKisi}
    return render(request,"front_end/list/detay_kisi.html",context)    

def list(request): 
    detay =KisiDetay.objects.all()
    print(detay)
    context={'detay':detay}
    return render(request, 'front_end/list/index.html',context)

def blog(request): 
    context = {}
    return render(request,"front_end/blog/index.html",context)

def blog_detail(request): 
    context = {}
    return render(request,"front_end/blog/index_details.html",context)

def about(request): 
    context = {}
    return render(request,"front_end/about/index.html",context)

def contact(request): 
    context = {}
    return render(request,"front_end/contact/index.html",context)

@csrf_exempt
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("website:login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request,"front_end/login/register.html", {"register_form":form})

@csrf_exempt
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("website:home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request,"front_end/login/login.html", {"login_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("website:login")



########################################
def admin_blog_category(request):
    blog_category = BlogCategory.objects.all()
    if request.user.is_anonymous:
        return redirect('website:home')
    if request.method == 'POST':
        category_name = request.POST.get("category")
        BlogCategory.objects.create(name=category_name)
    context = {'blog_category':blog_category}
    return render(request,"back_end/admin_blog_category/index.html",context)

def blog_category_delete(request):
    id = request.POST.get("delete")
    category = BlogCategory.objects.get(id = id )
    category.delete()
    return redirect(request.META.get('HTTP_REFERER'))

def blog_category_update(request,id):
    category = BlogCategory.objects.get(id = id)
    if request.method == 'POST':
        data = request.POST.get("category")
        category.name = data
        category.save()
    context = {'category':category}
    return render(request,"back_end/admin_blog_category/update_blog_category.html",context)

def admin_blog(request):
    if request.user.is_anonymous:
        return redirect('website:home')
    form = blogForm()
    if request.method == 'POST':
        form = blogForm(request.POST  or None,request.FILES  or None)
        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER'))
    getBlog = blogBilgi.objects.all().order_by('-id')
    context = {'form':form, 'blogBilgi':getBlog}
    return render(request,"back_end/admin_blog/index.html",context)


def update_blog(request,id):
    if request.user.is_anonymous:
        return redirect('website:home')
    blog = blogBilgi.objects.get(id = id)
    form = blogForm(instance=blog)
    if request.method == 'POST':
        form =  blogForm(request.POST or None, request.FILES or None, instance=blog)
        form.save()
        return redirect(request.META.get('HTTP_REFERER'))
    getBlog = blogBilgi.objects.all()
    context={'form':form,'blog':blog,'blogBilgi':getBlog}
    return render(request,"back_end/admin_blog/update_blog.html",context)





def deleteBlog(request):
    if request.method == 'POST':
        blogBilgi.objects.get(id=request.POST.get('delete')).delete()
    return redirect(request.META.get('HTTP_REFERER'))
 #########################################################    





 