import requests
import random

class TestMainCase:
    token=''
    draftId=''
    ip='http://183.60.233.74'
    def test_silentAuthorization(self):
        url = TestMainCase.ip+'/iss-dmz/channelAuthorization/silentAuthorization'
        params='channelUserId=6lfgx1P9HxtShRtGbZ88o3OVocr+jxsjZ0fCZ+0LkKlEec8WIvizvGUUd2rJP9yYMXl/klck+PEWTz0/hZO7AQ=='
        requestReturn = requests.request(method='post',url=url,params= params).json()
        TestMainCase.token=requestReturn['data']['token']
        print(requestReturn)

    def test_checkProduct(self):
        url=TestMainCase.ip+'/iss-dmz/channel/checkProduct'
        headers={'channelAuthorization':TestMainCase.token}
        data={"productCode":"1665"}
        requestReturn = requests.request(method='post',url=url,headers=headers,json=data).json()
        print(requestReturn)

    def test_mainInsurance(self):
        url=TestMainCase.ip+'/iss-dmz/iclient/nbi/emp/li/channel/selectmain/maininsurance.do'
        headers={'channelAuthorization':TestMainCase.token}
        data={
            "customerList": [
                {
                    "customerType": "2",
                    "name": "",
                    "sex": "M",
                    "birthday": "生日(选填)",
                    "profGrade": "1",
                    "profCode": "",
                    "profName": "选择职业",
                    "relationShipCode": "",
                    "relationShipName": "",
                    "relationShipRemark": "",
                    "isInsurantMedicare": "",
                    "compensationMedicalPlanFlag": ""
                },
                {
                    "customerType": "1",
                    "name": "",
                    "sex": "M",
                    "age": "30",
                    "birthday": "生日(选填)",
                    "profGrade": "1",
                    "profCode": "",
                    "profName": "选择职业",
                    "isInsurantMedicare": "",
                    "compensationMedicalPlanFlag": ""
                }
            ],
            "draftId": "",
            "planCode": "1665"
        }
        requestReturn = requests.request(method='post',url=url,headers=headers,json=data).json()
        TestMainCase.draftId=requestReturn['data']['draftId']
        print(requestReturn)

    def test_setTraceInfo(self):
        url = TestMainCase.ip + '/iss-dmz/trace/setTraceInfo'
        headers = {'channelAuthorization': TestMainCase.token}

        data = {
          "draftId":TestMainCase.draftId,
          "traceId":"PACZ202208100312000000000"+str(random.randint(1,1000))
        }
        requestReturn = requests.request(method='post', url=url, headers=headers, json=data).json()
        print(requestReturn)


if __name__ == '__main__':
    TestMainCase().test_silentAuthorization()
    TestMainCase().test_checkProduct()
    TestMainCase().test_mainInsurance()
    TestMainCase().test_setTraceInfo()