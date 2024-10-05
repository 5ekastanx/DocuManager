import requests

class ValidPhone:
    def __init__(self, phone):
        self.phone: str = phone
        self.url: str = "https://phonevalidation.abstractapi.com/v1/?api_key=9b1be51fef784662945af53322de3ed2&phone="

    def request_from_the_api(self):
        reponse = requests.get(url=self.url + self.phone)
        if reponse.status_code != 200:
            return {'valid': False}
        return response.json()
    
    def information_about_the_phone_number(self) -> dict:
        data: dict = self.request_from_the_api()
        if not data:
            return {'valid': False}
        
        return dict(data)