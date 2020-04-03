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
    try:
        if request.GET['cities']:
            gungus=Gungu.objects.filter(sd_name_id=request.GET['cities'])
    except:
        print("pass")
        pass
    return render(request, 'index.html', 
    {'cities' : cities, 'gungus' :gungus, 'candidates':candidates, 'parties':parties, 'partypolicies':partypolicies})
