from django.shortcuts import render
from get_data.models import Party, PartyPolicy, City, Gungu, Candidate 
import urllib.request
from urllib.parse import urlencode,quote_plus


# Create your views here.
def index(request):
    cities = City.objects
    gungus = ""
    candidates = Candidate.objects
    parties = Party.objects
    partypolicies = PartyPolicy.objects
    temp_cities = None

    # try:
    if request.GET.get('cities'):
        # gungus=Gungu.objects.filter(sd_name_id=request.GET['cities'])
        gungus=Gungu.objects.filter(sd_name = City.objects.get(name=request.GET['cities']))
        temp_cities = request.GET.get('cities')
    # except:
    #     print("pass")
    #     pass
    context = {'cities' : cities, 'temp_cities':temp_cities, 'gungus' :gungus, 'candidates':candidates, 'parties':parties, 'partypolicies':partypolicies}
    return render(request, 'index.html', context)
