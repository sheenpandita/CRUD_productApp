from django.shortcuts import render,HttpResponseRedirect
from .models import pro
from application.forms import productpage

# Create your views here.
#This view will add new item to database
def add_show(request):
    if request.method == 'POST':
        display = pro.objects.all()
        fm = productpage(request.POST, request.FILES)
        if fm.is_valid():
            nm = fm.cleaned_data['item_name']
            pr = fm.cleaned_data['price']
            des = fm.cleaned_data['desc']
            im = fm.cleaned_data['img']
            reg = pro(item_name=nm,price=pr,desc=des,img=im)
            reg.save()
            fm = productpage()
    else:
         fm = productpage()
    display = pro.objects.all()
    return render(request, 'application/addandshow.html',{'form':fm, 'dis':display})

#this view  deletes data from database
def delete_data(request, id):
    if request.method == 'POST':
        pi = pro.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')

#this view updates existing data
def update_data(request, id):
    if request.method == "POST":
        pi = pro.objects.get(pk=id)
        fm = productpage(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        else:
            pi = pro.objects.get(pk=id)
            fm = productpage(instance=pi)     
    return render(request,'application/update.html', {'form':fm})
    