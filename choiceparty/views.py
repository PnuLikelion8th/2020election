from django.shortcuts import render
from get_data.models import Party
import random
# Create your views here.
def blind_party(request):
    # temp_list=list(range(1, 52))
    # random.shuffle(temp_list)
    # print(temp_list)

    if request.method == 'POST':
        #넘어오는 쿼리를 dict으로 해서 muttable하게 해준다.
        tmp_dict = dict(request.POST)
        # 토큰 제거
        del tmp_dict['csrfmiddlewaretoken']
        
        #dict에서 value값인 정당 가져오기
        tmp_list = list(tmp_dict.values())
        random.shuffle(tmp_list)

        len_tmp_party = len(tmp_list)

        divider_num = len_tmp_party//2

    
        if len_tmp_party % 2 == 1:
            msg = "누군가 부전승으로 올라갔습니다."
            unearned = tmp_list[len_tmp_party-1]

            top = tmp_list[0:divider_num]
            bottom = tmp_list[divider_num:len_tmp_party-1]
        else:
            msg = None
            unearned = None

            top = tmp_list[0:divider_num]
            bottom = tmp_list[divider_num:len_tmp_party]
       

        context = {'all_party': tmp_list, 'len_party': len_tmp_party,
                   'top': top, 'bottom': bottom, 'msg': msg, 'unearned': unearned}

        return render(request, 'blind_party.html', context)
        
    else:
        all_party = Party.objects.exclude(name="무소속").prefetch_related('partypolicy_set').order_by('?')

        len_party = len(all_party)

        divider_num = len_party//2

        if len_party % 2 == 1:
            msg = "누군가 부전승으로 올라갔습니다."
            unearned = all_party[len_party-1]
            
            top = all_party[0:divider_num]
            bottom = all_party[divider_num:len_party-1]

        else:
            msg = None
            unearned = None

            top = all_party[0:divider_num]
            bottom = all_party[divider_num:len_party]
        
        context = {'all_party': all_party, 'len_party': len_party,
                'top': top, 'bottom': bottom, 'msg': msg, 'unearned': unearned}

        return render(request , 'blind_party.html',context)
