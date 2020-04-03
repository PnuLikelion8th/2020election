from django.shortcuts import render




import urllib.request
from urllib.parse import  urlencode,quote_plus


# Create your views here.
def index(request):
    url = 'http://apis.data.go.kr/9760000/ElecPrmsInfoInqireService/getCnddtElecPrmsInfoInqire'
    serviceKey = 'Xvpo0Pb%2BjhwLSMLl8Ao5IyZmL6rmcm2T9XrNr6h3UQ2cb1nHi33PjKupqsOsOnIQvgfqNDRQ5fTDh7g3c%2BVNFg%3D%3D'
    queryParams = '?pageNo=1&numOfRows=10&resultType=xml&sgId=20170509&sgTypecode=1&cnddtId=1000000000&ServiceKey='+serviceKey
    # '?' + urlencode({ quote_plus('ServiceKey') : '서비스키', quote_plus('ServiceKey') : 'Mgaohpr2wBuGBThVLkQdfSyLhtj3N0lMeju59DM7SwYMFlvE8AoJZASKowr59UZw18q2S5JvUrO75PAPr%2BVLPQ%3D%3D', quote_plus('pageNo') : '1', quote_plus('numOfRows') : '10', quote_plus('sgId') : '20170509', quote_plus('sgTypecode') : '1', quote_plus('cnddtId') : '1000000000' })

    requests = urllib.request.Request(url + queryParams)
    requests.get_method = lambda: 'GET'
    response_body = urllib.request.urlopen(requests).read()
    
    return render(request,'index.html',{'res':response_body})
