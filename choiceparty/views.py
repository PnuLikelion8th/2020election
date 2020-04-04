from django.shortcuts import render
from get_data.models import Party
import random
# Create your views here.
def blind_party(request):
    # temp_list=list(range(1, 52))
    # random.shuffle(temp_list)
    # print(temp_list)
    all_party = Party.objects.prefetch_related('partypolicy_set').all().order_by('?')

    
    context = {'all_party': all_party}

    return render(request , 'blind_party.html',context)
