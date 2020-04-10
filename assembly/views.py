from django.shortcuts import render
from get_data.models import Party, PartyPolicy, City, Gungu, Candidate 



def main(request):
    return render(request, 'main.html')

def index(request):
    cities = City.objects
    gungus=Gungu.objects.filter(sd_name = City.objects.get(name='부산광역시'))
    candidates = Candidate.objects
    parties = Party.objects
    partypolicies = PartyPolicy.objects

    if request.GET.get('gungus'):
        temp_gungus = Gungu.objects.get(id=request.GET.get('gungus'))
        target_candidates = candidates.filter(sggname=temp_gungus)
        search_video_q = '부산광역시' + temp_gungus.sgg_name
        context = {'cities' : cities, 'gungus' :gungus,'temp_gungus':temp_gungus, 'candidates':candidates,
                   'target_candidates': target_candidates, 'parties': parties, 'partypolicies': partypolicies, 'search_video_q': search_video_q}
        return render(request, 'index.html', context)


    

    gungus=Gungu.objects.filter(sd_name = City.objects.get(name='부산광역시'))
    temp_cities = request.GET.get('cities')
    context = {'cities' : cities, 'temp_cities':temp_cities, 'gungus' :gungus, 'candidates':candidates, 'parties':parties, 'partypolicies':partypolicies}
    return render(request, 'index.html', context)
