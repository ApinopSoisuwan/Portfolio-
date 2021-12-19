from django.shortcuts import render



# Create your views here.

def layout (request):
    return render(request,"layout.html")

def home (request):
    return render(request,"home.html")

def diary (request):
    return render(request,"diary.html")
