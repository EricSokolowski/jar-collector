from django.shortcuts import render



# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def jars_index(request):
  return render(request, 'jars/index.html', { 'jars': jars})

class Jar:
  def __init__(self, name, contents, description, type):
    self.name = name
    self.contents = contents
    self.description = description
    self.type = type

jars = [
  Jar('Happy Jar', 'Grape Jelly', 'Nice looking Mason Jar', 'Mason'),
  Jar('Cool Jar', 'Strawberry Jelly', 'oh yeah jar', 'Mason')

]