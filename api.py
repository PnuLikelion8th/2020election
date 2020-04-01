from urllib import request
import urllib.request
from urllib.parse import  urlencode,quote_plus

url = 'http://apis.data.go.kr/9760000/ElecPrmsInfoInqireService/getCnddtElecPrmsInfoInqire'
serviceKey = 'Xvpo0Pb%2BjhwLSMLl8Ao5IyZmL6rmcm2T9XrNr6h3UQ2cb1nHi33PjKupqsOsOnIQvgfqNDRQ5fTDh7g3c%2BVNFg%3D%3D'
queryParams = '?pageNo=1&numOfRows=10&resultType=xml&sgId=20170509&sgTypecode=1&cnddtId=1000000000&ServiceKey='+serviceKey

request = request.Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urllib.request.urlopen(request).read()
print(response_body)


