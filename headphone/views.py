from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = 'Yangon'
    dest1.desc = 'The City that Never Sleeps'
    dest1.price = 700
    dest1.image = 'yangon.jpg'

    dest2 = Destination()
    dest2.name = 'Mandalay'
    dest2.desc = 'The City that Never Sleeps'
    dest2.price = 600
    dest2.image = 'yangon2.jpg'

    dest3 = Destination()
    dest3.name = 'Mawlamying'
    dest3.desc = 'The City that Never Sleeps'
    dest3.price = 300
    dest3.image = 'yangon.jpg'

    dests = [dest1, dest2, dest3 ]

    return render(request, 'index.html',{'dests':dests})
