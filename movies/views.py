from django.shortcuts import render

categories =["macera", "romantik", "dram","bilim kurgu"]

def home(request):
  data = {
    "categories" : categories
  }
  return render(request, 'index.html',data)

def movies(request):
  return render(request, 'movies.html')