from django.shortcuts import render
from get_data.models import Party, PartyPolicy, City, Gungu, Candidate 
import urllib.request
from urllib.parse import  urlencode,quote_plus


# Create your views here.
def index(request):
    cities = City.objects
    gungus = Gungu.objects
    return render(request, 'index.html', {'cities' : cities})
