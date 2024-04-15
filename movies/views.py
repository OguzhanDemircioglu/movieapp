from django.shortcuts import render

categories = ["macera", "romantik", "dram", "bilim kurgu"]
films = [
  {
    "id": 1,
    "title": "Flim1",
    "description": "Flim1 description",
    "image": "1.jpg",
    "anasayfa": True
  },
  {
    "id": 2,
    "title": "Flim2",
    "description": "Flim2 description",
    "image": "2.jpg",
    "anasayfa": True
  },
  {
    "id": 3,
    "title": "Flim3",
    "description": "Flim3 description",
    "image": "3.jpg",
    "anasayfa": False
  },
  {
    "id": 4,
    "title": "Flim4",
    "description": "Flim4 description",
    "image": "4.jpg",
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
  return render(request, 'movies.html', data)


def movieDetails(request, id):
  data = {
    "id": id
  }
  return render(request, 'details.html', data)
