from django.shortcuts import render

def func4(request):
    return render(request,'app4.html')
# Create your views here.

def count(request):
    fulltext=request.GET['fulltext']
    fulltext1=request.GET['fulltext1']
    
    return render(request,'count.html',{'lll':fulltext, 'jjj':fulltext1})
