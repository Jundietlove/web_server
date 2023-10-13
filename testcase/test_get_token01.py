import pytest
import requests

class Testgettoken:

    token=""

    def test_get_token(self):
        url = "http://office.asiatic.cc:7399/portal-api/mp/home/token"
        data = {
            "mallId": "1511608353875435521",
            "openId": "o7G8Y0TBpapPH8ZGFVrpFLHmun7Y",
            "unoinId": "oL1CSwJAwQB-cJjlAOfel-nbLxZ8"
        }

        rep = requests.get(url=url, params=data)
        print(rep.json())
        Testgettoken.token=rep.json()['token']

    def test_addInvoice(self):
            url = "http://office.asiatic.cc:7399/portal-api/mp/omni/addInvoice"+Testgettoken.token
            data = {"mallId": "1622792807807803393",
                    "invoiceHeader": "string",
                    "invoiceTax": "string",
                    "invoiceMail": "string@"}
            rep = requests.get(url=url, json=data)
            print(rep.json())

if __name__=='__main__':
    pytest.main('-vs')


