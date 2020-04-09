from django.shortcuts import render,redirect
from .models import Party, PartyPolicy, City,Gungu,Candidate
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

URL2 = 'http://apis.data.go.kr/9760000/CommonCodeService/getCommonSggCodeList?serviceKey=1xchWYQzhGHEZWwvB6UCLFzMCUxgox9p4lZ%2Fbj8%2FaOTeSBZ0cA4NCQt%2BLMgPTljOOxFBjJA5CuFsDfynkT0HXw%3D%3D&sgId=20200415&sgTypecode=2&resultType=json'

def makecity(request):
    pagenum_list = [1, 2, 3]
    # del_gungu = Gungu.objects.all()
    # del_gungu.delete()
   
    # for pagenum in pagenum_list:
    #     resp = requests.get(URL2+'&pageNo=' + str(pagenum) +'&numOfRows=100')
    #     json_result = json.loads(resp.text)
    #     city_list = json_result['getCommonSggCodeList']['item']
        
    #     for j in city_list:
    #         Gungu.objects.create(sd_name=City.objects.get(
    #             name=j['SD_NAME']), name=j['WIW_NAME'], sgg_name=j['SGG_NAME'])
    #         print(j['SD_NAME'], j['WIW_NAME'], '-', j['SGG_NAME'])



            # if City.objects.filter(name=j['SD_NAME']).exists():
            #     pass
            # else:
            #     City.objects.create(name=j['SD_NAME'])
    return redirect('index')


URL3 = 'http://apis.data.go.kr/9760000/PofelcddInfoInqireService/getPofelcddRegistSttusInfoInqire?serviceKey=1xchWYQzhGHEZWwvB6UCLFzMCUxgox9p4lZ%2Fbj8%2FaOTeSBZ0cA4NCQt%2BLMgPTljOOxFBjJA5CuFsDfynkT0HXw%3D%3D&pageNo=1&numOfRows=1200&sgId=20200415&sgTypecode=2&resultType=json'

def makecandi(request):
    resp = requests.get(URL3)
    json_result = json.loads(resp.text)
    candi_list = json_result['getPofelcddRegistSttusInfoInqire']['item']
    index = 1
    for i in candi_list:
        Candidate.objects.create(
            candi_id=i['HUBOID'],
            sggname=Gungu.objects.get(
                sd_name=City.objects.get(name=i['SD_NAME']), sgg_name=i['SGG_NAME'], name=i['WIW_NAME']),
            giho_num=i['GIHO'],
            jdname=Party.objects.get(name=i['JD_NAME']),
            name=i['NAME'],
            gender=i['GENDER'],
            birth = i['BIRTHDAY'],
            age=i['AGE'],
            addr = i['ADDR'],
            job = i['JOB'],
            edu = i['EDU'],
            career1=i['CAREER1'],
            career2 = i['CAREER2'],
            status = i['STATUS']
        )
        print(str(index) + '...')
        index+=1
    # del_candi = Candidate.objects.all()
    # del_candi.delete()
    return redirect('index')


def makeattend(request):

    for i in Candidate.objects.all():
        print(i.name,i.jdname)

        
    return redirect('index')
