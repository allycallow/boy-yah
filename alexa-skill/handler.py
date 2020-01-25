import logging
from ask_sdk_core.utils import is_intent_name
from ask_sdk_core.skill_builder import SkillBuilder
from utils.api_services import ApiServices

sb = SkillBuilder()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@sb.request_handler(can_handle_func=is_intent_name("AMAZON.HelpIntent"))
def help_intent_handler(handler_input):
    logger.info("In HelpIntentHandler")
    handler_input.response_builder.speak("Boom Boom").ask("Please go again")
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=is_intent_name("BloodPressure"))
def blood_pressure_intent_handler(handler_input):
    logger.info(f"BloodPressure")
    response_builder = handler_input.response_builder

    print(handler_input.request_envelope.request)
    systolic_number = handler_input.request_envelope.request.intent.slots["systolic_number"].value
    diastolic_number = handler_input.request_envelope.request.intent.slots["diastolic_number"].value

    api_services = ApiServices()
    api_services.store_blood_pressure(systolic_number, diastolic_number)

    speech_text = f"working {systolic_number} {diastolic_number}"

    return response_builder.speak(speech_text).set_should_end_session(False).response


handler = sb.lambda_handler()
