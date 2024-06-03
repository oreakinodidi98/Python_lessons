from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import User
from .forms import UserForm

# Create your views here.
def view_home(request):
    return HttpResponse("hello worlld")

def user_list(request):
    records = User.objects.all()
    form_records = {'records' : records}
    # Render a template. It needs to be under the folder after
    # templates. templates/register_app
    return render(request,'listingpage.html',context=form_records)

def add_user(request):
    form_records = {}
    form = UserForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("home")
    form_records['form'] = form
    return render(request,'add.html', form_records)

def edit_user(request,id=None):
    one_rec = User.objects.get(pk=id)
    form = UserForm(request.POST or None,request.FILES or None, instance=one_rec)
    if form.is_valid():
        form.save()
        return redirect("home")
    form_records =  {'form':form}
    return render(request,'edit.html',context=form_records)

def delete_user(request,eid=None):
    one_rec = User.objects.get(pk=eid)
    if  request.method !="POST":
         one_rec.delete()
         return redirect("home")
    return render(request,'delete.html')

def view_user(request,eid=None):
    form_records = {}
    one_rec = User.objects.get(pk=eid)
    form_records['user'] = one_rec
    return render(request,"view.html", form_records)