from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Area,Profile,Business,Updates
from .forms import HoodForm,UpdateForm,BusinessForm
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
  business = Business.objects.all()

  updateform = UpdateForm(request.POST,request.FILES)
  if request.method == 'POST':
    
    if updateform.is_valid():
      update = updateform.save(commit=False)
      update.area = request.user.profile.neighbourhood
      update.author = request.user.profile
      update.save()
    return redirect('home',update_id)
  else:
    updateform = UpdateForm() 


  businessform = BusinessForm(request.POST,request.FILES)
  if request.method == 'POST':

    if businessform.is_valid():
      biz = businessform.save(commit=False)
      biz.area = request.user.profile.neighbourhood
      biz.author = request.user.profile
      businessform.save()
    return redirect('home',update_id)
  else:
      businessform = BusinessForm()
  
  context = {
    'updates':updates,
    'business':business,
    'updateform':updateform,
    'businessform':businessform,
  }


  return render(request,'index.html',context)

