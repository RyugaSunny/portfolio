from django.shortcuts import render

# Create your views here.
def index(r):
    return render(r,"index.html")

def portfolio_details(r):
    return render(r,"portfolio-details.html")