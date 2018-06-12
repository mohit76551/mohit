from django.shortcuts import render, HttpResponse

#Create view here
def home(request);
    return render(request, "first.html")