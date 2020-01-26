import requests
import json
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

API_ENDPOINT = "https://rest.ehrscape.com/rest/v1"
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
        r = requests.post(url="{API_ENDPOINT}/composition?ehrId=5f4401c5-071a-4b4e-8426-6f2ccb32fb04&templateId=NHSHD23%20BoYaA&committerName=Alexa&format=FLAT", data=json.dumps(data), headers=headers)

        print(r.status_code)
        print(r.json())

        if r.ok:
            logger.info("successfully stored record")
            return r.json()
        raise Exception("something went wrong")

    def store_peak_flow_rate(self, peak_flow_rate):
        logger.info("peak_flow_rate fired")
        data = {
            'ctx/composer_name': COMPOSER_NAME,
            "ctx/language": LANGUAGE,
            "ctx/territory": TERRITORY,
            "nhshd23_boyaa/peak_flow_rate/result_details/pulmonary_flow_rate_result/actual_result": peak_flow_rate,
            "nhshd23_boyaa/peak_flow_rate/result_details/pulmonary_flow_rate_result|unit": "l/min"
        }

        headers = {'content-type': 'application/json', "Authorization": f"Basic {TOKEN}"}
        r = requests.post(url=f"{API_ENDPOINT}/composition?ehrId=5f4401c5-071a-4b4e-8426-6f2ccb32fb04&templateId=NHSHD23%20BoYaA&committerName=Alexa&format=FLAT", data=json.dumps(data), headers=headers)

        print(r.status_code)
        print(r.json())

        if r.ok:
            logger.info("successfully stored record")
            return r.json()
        raise Exception("something went wrong")

    def get_csv(self):
        logger.info("get_csv")
        data = {
            "aql": "select a_a/data[at0001|Event Series|]/events[at0002|Any event|]/data[at0003]/items[at0127|Result details|]/items[at0057|Pulmonary flow rate result|]/items[at0058|Actual result|]/value/magnitude as Result_Value, a_a/data[at0001|Event Series|]/origin/value as Time, a_a/data[at0001|Event Series|]/events[at0002|Any event|]/state[at0031]/items[at0098|Confounding factors|]/value/value as Setting, a_a/data[at0001|Event Series|]/events[at0002|Any event|]/state[at0031]/items[at0049|Bronchodilation|]/items[at0051|Agent|]/value/value as Agent, a_a/data[at0001|Event Series|]/events[at0002|Any event|]/state[at0031]/items[at0049|Bronchodilation|]/items[at0091|Timing|]/value/value as Challenge_State from EHR e contains COMPOSITION a contains OBSERVATION a_a[openEHR-EHR-OBSERVATION.pulmonary_function.v0] order by a_a/data[at0001|Event Series|]/origin/value desc"
        }

        headers = {'content-type': 'application/json', "Authorization": f"Basic {TOKEN}"}
        r = requests.post(url=f"{API_ENDPOINT}/query/csv", data=json.dumps(data), headers=headers)

        print(r.status_code)
        print(r.json())

        if r.ok:
            logger.info("successfully stored record")
            return r.json()
        raise Exception("something went wrong")
