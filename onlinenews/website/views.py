from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'website/home.html')
def bolly_view(request):
    return render(request,'website/bolly.html')
def politic_view(request):
    return render(request,'website/politics.html')
def sport_view(request):
    return render(request,'website/sport.html')
