from django.shortcuts import render,redirect
from .models import Party,PartyPolicy
import json
import requests

URL = 'http://apis.data.go.kr/9760000/PartyPlcInfoInqireService/getPartyPlcInfoInqire'
DAY = "20200415"
API_KEY = '?serviceKey=1xchWYQzhGHEZWwvB6UCLFzMCUxgox9p4lZ%2Fbj8%2FaOTeSBZ0cA4NCQt%2BLMgPTljOOxFBjJA5CuFsDfynkT0HXw%3D%3D'
PARTY = ['더불어민주당', '미래통합당', '민생당', '미래한국당', '더불어시민당', '정의당',
         '우리공화당', '민중당', '한국경제당', '국민의당', '친박신당', '열린민주당', '코리아',
         '가자!평화인권당', '가자환경당', '공화당', '국가혁명배당금당', '국민새정당', '국민참여신당', '기독당',
         '기독자유통일당', '기본소득당', '깨어있는시민연대당', '남북통일당', '노동당', '녹색당', '대한당', '대한민국당',
         '미래당', '미래민주당', '미래자영업당', '민중민주당', '사이버모바일국민정책당', '새누리당', '시대전환', '여성의당',
         '우리당', '자유당', '새벽당', '정치개혁연합', '자영업당', '직능자영업당', '충청의미래당', '친박연대', '통일민주당', '통합민주당',
         '한국국민당', '한국복지당', '한나라당', '한반도미래연합', '홍익당']

def makeparty(request):
    # for i in PARTY:
    #     Party.objects.create(name=i)

    

    # for i in PARTY:
    #     print(i,"...........")
    #     resp = requests.get(URL + API_KEY + '&sgId='+DAY +
    #                         '&partyName='+ i +'&resultType=json')
    #     py_json = json.loads(resp.text)
    #     if py_json['getPartyPlcInfoInqire']['item'] != []:
    #         target = py_json['getPartyPlcInfoInqire']['item'][0]
    #         for j in range(1, 11):
    #             if target['prmsTitle'+str(j)] == "":
    #                 break

    #             PartyPolicy.objects.create(
    #                 name= Party.objects.get(name = i), number=j, title=target['prmsTitle'+str(j)],
    #                 category=target['prmsRealmName'+str(j)],
    #                 desc=target['prmmCont'+str(j)])

    # del_party = PartyPolicy.objects.all()
    # del_party.delete()
    return redirect('index')
