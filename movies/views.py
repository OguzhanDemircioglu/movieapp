from django.shortcuts import render

categories = ["macera", "romantik", "dram", "bilim kurgu"]
films = [
  {
    "title": "Flim1",
    "description": "Flim1 description",
    "image": "1.jpg",
    "anasayfa": True
  },
  {
    "title": "Flim2",
    "description": "Flim2 description",
    "image": "2.jpg",
    "anasayfa": True
  },
  {
    "title": "Flim3",
    "description": "Flim3 description",
    "image": "3.jpg",
    "anasayfa": False
  }
]

def home(request):
  data = {
    "categories": categories,
    "films": films
  }
  return render(request, 'index.html', data)

def movies(request):
  data = {
    "categories": categories,
    "films": films
  }
  return render(request, 'movies.html',data)
