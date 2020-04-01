from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
import json

from django.shortcuts import render

# Create your views here.
def promise(request):
    url = "http://apis.data.go.kr/9760000/PofelcddInfoInqireService"
    queryParams = '?' + urlencode({
    # quote_plus('ServiceKey'): 'Mgaohpr2wBuGBThVLkQdfSyLhtj3N0lMeju59DM7SwYMFlvE8AoJZASKowr59UZw18q2S5JvUrO75PAPr%2BVLPQ%3D%3D', 
    quote_plus('ServiceKey'): 'CiN%2FaMLI7zYq2yK3VRDZwXXkPLboTGDZ7XgC4MLBRJJUV%2FErugk0uaqW9PD5i5Ru2BpvZw8LLDXY1nrXe7TBDw%3D%3D',
    quote_plus('pageNo'):'1',
    quote_plus('numOfRows'):'10',
    quote_plus('sgld'): '20180613',
    quote_plus('sgTypecode'):'4',
    quote_plus('cnddtld'):'1000000000'})

    request = Request(url + queryParams)
    request.get_method = lambda:'GET'
    response_body = urlopen(request).read()
    return (response_body, 'map.html')

    # url = "http://apis.data.go.kr/9760000/ElecPrmsInfoInqireService"
    # queryParams = '?' + urlencode({
    # # quote_plus('ServiceKey'): 'Mgaohpr2wBuGBThVLkQdfSyLhtj3N0lMeju59DM7SwYMFlvE8AoJZASKowr59UZw18q2S5JvUrO75PAPr%2BVLPQ%3D%3D', 
    # quote_plus('ServiceKey'): 'Xvpo0Pb%2BjhwLSMLl8Ao5IyZmL6rmcm2T9XrNr6h3UQ2cb1nHi33PjKupqsOsOnIQvgfqNDRQ5fTDh7g3c%2BVNFg%3D%3D',
    # quote_plus('pageNo'):'1',
    # quote_plus('numOfRows'):'10',
    # quote_plus('sgld'): '20170509',
    # quote_plus('sgTypecode'):'1',
    # quote_plus('cnddtld'):'1000000000'})

    # request = Request(url + queryParams)
    # request.get_method = lambda:'GET'
    # response_body = urlopen(request).read()
    # return (response_body, 'map.html')
