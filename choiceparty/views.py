from django.shortcuts import render
from get_data.models import Party
from django.db.models import Q
from functools import reduce

import random


# Create your views here.
def blind_party(request):
    # temp_list=list(range(1, 52))
    # random.shuffle(temp_list)
    # print(temp_list)

    if request.method == 'POST':
        #넘어오는 쿼리를 dict으로 해서 muttable하게 해준다.
        tmp_dict = dict(request.POST)
        print(request.POST, "=========쿼리==============")

        # 토큰 제거
        del tmp_dict['csrfmiddlewaretoken']
        # 우리가 받은 str을 Q set을 이용하여 복수개의 condition을 설정해준다
        multi_get_condition = [Q(name=i[0]) for i in list(tmp_dict.values())]
        condi_q = reduce(lambda  x,y: x | y, multi_get_condition)
        tmp_list = Party.objects.filter(condi_q).order_by(
            '?').prefetch_related('partypolicy_set')


        len_tmp_party = len(tmp_list)
        print(len_tmp_party,"=========길이==============")
        #마지막에 1개 남았을때는 우리가 끝났다는것을 알려줘야함
        if len_tmp_party == 1:
            print("끝났습니다")
            context = {'all_party': tmp_list}
            #이정도로만 보내고 나머지는 template에서 lenth체크를 해줘서 if문 걸꺼임
            return render(request, 'blind_party.html', context)


        divider_num = len_tmp_party//2

    
        if len_tmp_party % 2 == 1:
            
            unearned = tmp_list[len_tmp_party-1]
            msg = str(unearned) + " 부전승으로 올라갔습니다."

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
            unearned = all_party[len_party-1]
            msg = str(unearned) + " 부전승으로 올라갔습니다."

            
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
