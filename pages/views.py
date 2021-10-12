from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    # return HttpResponse("<h1>Hii world</h1>")
    return render(request, "home.html", {})


def contact(request):
    return render(request, "contact.html")


def about(request):
    print(request.user)
    context = {
        "mytitle": "this is about me",
        "body": "body of the mind",
        "mylist": [123, 456, 789],
        "html":"<p>Dustttt</p>"
    }
    return render(request, "about.html", context)
