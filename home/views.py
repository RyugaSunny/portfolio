from django.shortcuts import render

# Create your views here.
def index(r):
    return render(r,r"home/index.html")
