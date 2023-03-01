from django.shortcuts import render

def func4(request):
    return render(request,'app4.html')
# Create your views here.

def count(request):
    fulltext=request.GET['fulltext']
    return render(request,'count.html',{'fulltext':fulltext})
