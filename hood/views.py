from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Area,Profile,Business,Updates
from .forms import HoodForm,UpdateForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login')
def area(request):
  area = Area.objects.all()
  
  return render(request,'areas.html',{'area':area})

@login_required(login_url='/accounts/login/')
def home(request,update_id):
  
  area = Area.objects.get(id = update_id)
  businesses = Business.area_businesses(area.id)
  updates = Updates.area_updates(area.id)
  # form = PostForm(request.POST,request.FILES)

  # if request.method == 'POST':
    
  #   if form.is_valid():
  #     post = form.save(commit=False)
  #     post.author = request.user.profile
  #     post.area = request.user.profile.neighbourhood
  #     post.save()
  #     return redirect('home',update_id) 
  #   else:
  #     form = PostForm()

  # context = {
  #   'area': area,
  #   'form': form,
    
  #  }

  return render(request,'index.html',{'updates':updates,'businesses':businesses})

def update(request):


  
  form = UpdateForm(request.POST,request.FILES)
  if request.method == 'POST':
    
    if form.is_valid():
      update = form.save(commit=False)
      update.area = request.user.profile.neighbourhood
      update.author = request.user.profile
      update.save()
      return redirect('area')
    else:
      form = UpdateForm()

  context = {
  
      'form':form,
    }

  return render(request,'newupdate.html',context)

def business(request):

  form = BusinessForm(request.POST,request.FILES)
  if request.method == 'POST':

    if form.is_valid():
      biz = form.save(commit=False)
      biz.area = request.user.profile.neighbourhood
      