from django.shortcuts import render
from get_data.models import Party, PartyPolicy, City, Gungu, Candidate 





def index(request):
    cities = City.objects
    gungus = None
    candidates = Candidate.objects
    parties = Party.objects
    partypolicies = PartyPolicy.objects
    

    if request.GET.get('gungus'):
        gungus=Gungu.objects.filter(sd_name = City.objects.get(name=request.GET['bf_cities']))
        temp_cities = request.GET.get('bf_cities')
        temp_gungus = Gungu.objects.get(id=request.GET.get('gungus'))
        print(temp_gungus)
        try:
            target_candidates = candidates.filter(sggname=temp_gungus)
        except:
            target_candidates = None
        # print([qs if qs.Exist else 'None' for qs in candidates.filter(sggname=Gungu.objects.get(name=temp_gungus))])
        context = {'cities' : cities, 'temp_cities':temp_cities, 'gungus' :gungus,'temp_gungus':temp_gungus, 'candidates':candidates,'target_candidates':target_candidates, 'parties':parties, 'partypolicies':partypolicies}
        return render(request, 'index.html', context)


    

    gungus=Gungu.objects.filter(sd_name = City.objects.get(name='부산광역시'))
    temp_cities = request.GET.get('cities')
    context = {'cities' : cities, 'temp_cities':temp_cities, 'gungus' :gungus, 'candidates':candidates, 'parties':parties, 'partypolicies':partypolicies}
    return render(request, 'index.html', context)
