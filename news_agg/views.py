from django.shortcuts import render
from django.http import JsonResponse
from .modules.websites.screen_rant import ScreenRant
from .modules.websites.collider import Collider
from .modules.websites.ign import Ign

from .modules.websites_manager import WebsiteManager


def index(request):

    manager = WebsiteManager()
    manager.add_website(ScreenRant())
    manager.add_website(Collider())
    manager.add_website(Ign())

    manager.fetch()

    context = manager.get_data()

    
    return JsonResponse({'websites': context}, safe=True)

def front_end(request):
    return render(request, 'front-end.html')
