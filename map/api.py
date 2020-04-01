from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
import json

url = "http://apis.data.go.kr/9760000/ElecPrmsInfoInqireService"
queryParams = '?' + urlencode({
# quote_plus('ServiceKey'): 'Mgaohpr2wBuGBThVLkQdfSyLhtj3N0lMeju59DM7SwYMFlvE8AoJZASKowr59UZw18q2S5JvUrO75PAPr%2BVLPQ%3D%3D', 
quote_plus('ServiceKey'): 'Mgaohpr2wBuGBThVLkQdfSyLhtj3N0lMeju59DM7SwYMFlvE8AoJZASKowr59UZw18q2S5JvUrO75PAPr%2BVLPQ%3D%3D',
quote_plus('pageNo'):'1',
quote_plus('numOfRows'):'10',
quote_plus('sgld'): '20170509',
quote_plus('sgTypecode'):'1',
quote_plus('cnddtld'):'1000000000'})

request = Request(url + queryParams)
request.get_method = lambda:'GET'
response_body = urlopen(request).read()
print (response_body)