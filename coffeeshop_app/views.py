from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import ModeForm
from .models import shop
# Create your views here.
def coffeeshop(request):
    product=shop.objects.all()
    return render(request,"home.html",{'products':product})
def detail(request,book_id):
    product1=shop.objects.get(id=book_id)
    return render(request,"detail.html",{'product':product1})
def add_product(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        img=request.FILES['img']
        s=shop(name=name,desc=desc,img=img)
        s.save()
        print("product added")
    return render(request,"add_product.html")
def update(request,id):
    obj=shop.objects.get(id=id)
    form=ModeForm(request.POST or None,request.FILES,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,"edit.html",{'form':form,'obj':obj})
def delete(request,id):
    if request.method=='POST':
        obj=shop.objects.get(id=id)
        obj.delete()
        return redirect('/')
    return render(request,"delete.html")


