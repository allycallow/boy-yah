import logging
from ask_sdk_core.utils import is_intent_name, is_request_type
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_model.ui import SimpleCard
from utils.api_services import ApiServices
from utils.email_services import EmailServices

sb = SkillBuilder()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@sb.request_handler(can_handle_func=is_request_type("LaunchRequest"))
def launch_request_handler(handler_input):
    """Handler for Skill Launch."""
    speech_text = "Welcome to the Alexa Skills Kit, you can say hello!"

    return handler_input.response_builder.speak(speech_text).set_card(
        SimpleCard("Hello World", speech_text)).set_should_end_session(
        False).response


@sb.request_handler(can_handle_func=is_intent_name("AMAZON.HelpIntent"))
def help_intent_handler(handler_input):
    logger.info("In HelpIntentHandler")
    handler_input.response_builder.speak("Boom Boom").ask("Please go again")
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=is_intent_name("StoreBloodPressure"))
def blood_pressure_intent_handler(handler_input):
    logger.info(f"StoreBloodPressure")
    response_builder = handler_input.response_builder

    print(handler_input.request_envelope.request)
    systolic_number = handler_input.request_envelope.request.intent.slots["systolic_number"].value
    diastolic_number = handler_input.request_envelope.request.intent.slots["diastolic_number"].value

    api_services = ApiServices()
    api_services.store_blood_pressure(systolic_number, diastolic_number)

    email_services = EmailServices()
    email_services.send_mail()

    speech_text = f"working {systolic_number} {diastolic_number}"

    return response_builder.speak(speech_text).set_should_end_session(False).response


@sb.request_handler(can_handle_func=is_intent_name("StorePeakFlowRate"))
def peak_flow_rate_intent_handler(handler_input):
    logger.info(f"StorePeakFlowRate")
    response_builder = handler_input.response_builder

    print(handler_input.request_envelope.request)
    peak_flow_rate = handler_input.request_envelope.request.intent.slots["peak_flow_rate"].value

    api_services = ApiServices()
    api_services.store_peak_flow_rate(peak_flow_rate)

    speech_text = f"working {peak_flow_rate}"

    return response_builder.speak(speech_text).set_should_end_session(False).response


@sb.exception_handler(can_handle_func=lambda i, e: True)
def all_exception_handler(handler_input, exception):
    """Catch all exception handler, log exception and
    respond with custom message.
    """
    # type: (HandlerInput, Exception) -> Response
    logger.error(exception, exc_info=True)

    speech = "Sorry, there was some problem. Please try again!!"
    handler_input.response_builder.speak(speech).ask(speech)

    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=is_intent_name("SendToDoctor"))
def send_to_doctor_intent_handler(handler_input):
    logger.info(f"SendToDoctor")
    response_builder = handler_input.response_builder

    email_services = EmailServices()
    email_services.send_mail()

    speech_text = f"Your doctor has now been sent your records."

    return response_builder.speak(speech_text).set_should_end_session(False).response


handler = sb.lambda_handler()
