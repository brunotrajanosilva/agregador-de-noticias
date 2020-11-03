from django.shortcuts import render
from django.http import HttpResponse
from .modules.ign_soup import ign_soup
from .modules.theenemy_soup import theenemy_soup
from .modules.create_and_sort_website_data import create_and_sort_website_data





def index(request):

    create_data = create_and_sort_website_data()
    ign = ign_soup()
    theenemy = theenemy_soup()

    create_data.add_website(ign)
    create_data.add_website(theenemy)

    news_result = create_data.sort_data()



    return render(request, 'index.html', {'results':news_result })