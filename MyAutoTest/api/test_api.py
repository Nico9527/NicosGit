import requests

class TestMainCase:
    result=''
    ip='http://183.60.233.74'
    def test_silentAuthorization(self):
        url = TestMainCase.ip+'/iss-dmz/channelAuthorization/silentAuthorization'
        params='channelUserId=6lfgx1P9HxtShRtGbZ88o3OVocr+jxsjZ0fCZ+0LkKlEec8WIvizvGUUd2rJP9yYMXl/klck+PEWTz0/hZO7AQ=='
        requestReturn = requests.request(method='post',url=url,params= params).json()
        TestMainCase.result=requestReturn['data']['token']
        print(requestReturn)

    def test_checkProduct(self):
        url=TestMainCase.ip+'/iss-dmz/channel/checkProduct'
        headers={'channelAuthorization':TestMainCase.result}
        data={"productCode":"1665"}
        requestReturn = requests.request(method='post',url=url,headers=headers,json=data).json()
        print(requestReturn)

if __name__ == '__main__':
    TestMainCase().test_silentAuthorization()
    TestMainCase().test_checkProduct()