from django.shortcuts import render
from get_data.models import Party, PartyPolicy, City, Gungu, Candidate 
import urllib.request
from urllib.parse import urlencode,quote_plus



def index(request):
    cities = City.objects
    gungus = None
    candidates = Candidate.objects
    parties = Party.objects
    partypolicies = PartyPolicy.objects
    

    if request.GET.get('gungus'):
        gungus=Gungu.objects.filter(sd_name = City.objects.get(name=request.GET['bf_cities']))
        # .get(name=request.GET['gungus']))
        temp_cities = request.GET.get('bf_cities')
        temp_gungus = request.GET.get('gungus')
        # # candidates = Candidate.objects.filter(sggname = Gungu.objects.get(name=request.GET['gungus']).sgg_name)
        # candidates = Candidate.objects.filter(sggname = Gungu.objects.get(name=request.GET['gungus']).sgg_name)
        # context = {'cities' : cities, 'temp_cities':temp_cities, 'gungus' :gungus,'temp_gungus':temp_gungus, 'candidates':candidates, 'parties':parties, 'partypolicies':partypolicies}
        try:
            target_candidates = candidates.filter(sggname=Gungu.objects.get(name=temp_gungus))
        except:
            target_candidates = None
        # print([qs if qs.Exist else 'None' for qs in candidates.filter(sggname=Gungu.objects.get(name=temp_gungus))])
        context = {'cities' : cities, 'temp_cities':temp_cities, 'gungus' :gungus,'temp_gungus':temp_gungus, 'candidates':candidates,'target_candidates':target_candidates, 'parties':parties, 'partypolicies':partypolicies}
        return render(request, 'index.html', context)


    elif request.GET.get('cities'):
        gungus=Gungu.objects.filter(sd_name = City.objects.get(name=request.GET['cities']))
        temp_cities = request.GET.get('cities')
        context = {'cities' : cities, 'temp_cities':temp_cities, 'gungus' :gungus, 'candidates':candidates, 'parties':parties, 'partypolicies':partypolicies}
        return render(request, 'index.html', context)

    temp_cities = None
    temp_gungus = None
    context = {'cities' : cities, 'temp_cities':temp_cities, 'gungus' :gungus, 'candidates':candidates, 'parties':parties, 'partypolicies':partypolicies}
    return render(request, 'index.html', context)


def who(request):
    whos = Candidate.objects.filter(sggname= Candidate.objects.get(name=request.GET['temp_gungus']))
    context = {'whos':whos}
    return render(request, 'index.html', context)
