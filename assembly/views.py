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
    # try:
    if request.GET.get('cities'):
        # gungus=Gungu.objects.filter(sd_name_id=request.GET['cities'])
        gungus=Gungu.objects.filter(sd_name = City.objects.get(name=request.GET['cities']))
    # except:
    #     print("pass")
    #     pass
    context = {'cities' : cities, 'gungus' :gungus, 'candidates':candidates, 'parties':parties, 'partypolicies':partypolicies}
    return render(request, 'index.html', context)