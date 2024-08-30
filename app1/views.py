from django.shortcuts import render
from app1.models import Author,Book
def home(request):
    result=Book.objects.all()
    return render(request,'index.html',{'books':result})

def createbook(request):
    if request.method=='POST':
        t=request.POST.get('bname')
        p=request.POST.get("price")
        g=request.POST.get("genre")
        s=request.POST.get('sno')
        a=Author.objects.get(id=s)
        if Author.objects.filter(id=s).exists():
            obj=Book.objects.create(title=t,price=p,genre=g,author=a)
            obj.save()
            return render(request,'createbook.html')
    return render(request,'createbook.html')

def createauthor(request):
    if request.method=='POST':
        name=request.POST.get('Aname')
        age=request.POST.get("age")
        rating=request.POST.get("rate")
        obj=Author(name=name,age=age,rating=rating)
        obj.save()

    return render(request,'create.html')
