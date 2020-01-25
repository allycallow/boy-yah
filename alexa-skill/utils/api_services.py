import requests
import json
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

API_ENDPOINT = "https://rest.ehrscape.com/rest/v1/composition?ehrId=5f4401c5-071a-4b4e-8426-6f2ccb32fb04&templateId=NHSHD23%20BoYaA&committerName=Alexa&format=FLAT"
TOKEN = "am9obi5tZXJlZGl0aEB3YWxlcy5uaHMudWs6ZWhyNGpvaG4ubWVyZWRpdGg="

COMPOSER_NAME = "Alexa"
LANGUAGE = "en"
TERRITORY = "GB"


class ApiServices:
    def store_blood_pressure(self, systolic_number, diastolic_number):
        logger.info("store_blood_pressure fired")
        data = {
            'ctx/composer_name': COMPOSER_NAME,
            "ctx/language": LANGUAGE,
            "ctx/territory": TERRITORY,
            "nhshd23_boyaa/blood_pressure/systolic|magnitude": systolic_number,
            "nhshd23_boyaa/blood_pressure/systolic|unit": "mm[Hg]",
            "nhshd23_boyaa/blood_pressure/diastolic|magnitude": diastolic_number,
            "nhshd23_boyaa/blood_pressure/diastolic|unit": "mm[Hg]"
        }

        headers = {'content-type': 'application/json', "Authorization": f"Basic {TOKEN}"}
        r = requests.post(url=API_ENDPOINT, data=json.dumps(data), headers=headers)

        print(r.status_code)
        print(r.json())

        if r.status_code == 200:
            logger.info("successfully stored record")
            return r.json()
        raise Exception("something went wrong")
