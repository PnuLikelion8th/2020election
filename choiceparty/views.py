from django.shortcuts import render
from get_data.models import Party
import random
# Create your views here.
def blind_party(request):
    # temp_list=list(range(1, 52))
    # random.shuffle(temp_list)
    # print(temp_list)
    all_party = Party.objects.exclude(name="무소속").prefetch_related('partypolicy_set').order_by('?')

    len_party = len(all_party)

    if len_party % 2 == 1:
        msg = "???정당이 부전승으로 올라갔습니다."
        unearned = all_party[len_party-1]

    else:
        msg = None
        unearned = None
    
    divider_num = len_party//2
    
    top = all_party[0:divider_num]
    bottom = all_party[divider_num:len_party-1]

    for i,k in enumerate(top):
        print(i,k)

    print("="*100)

    for j,v in enumerate(bottom):
        print(j,v)

    context = {'all_party': all_party, 'len_party': len_party,
               'top': top, 'bottom': bottom, 'msg': msg, 'unearned': unearned}

    return render(request , 'blind_party.html',context)
