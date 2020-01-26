import logging
from ask_sdk_core.utils import is_intent_name, is_request_type
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_model.ui import SimpleCard
from utils.api_services import ApiServices
from utils.email_services import EmailServices
from enum import Enum

sb = SkillBuilder()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class State(Enum):
    DO_YOU_WANT_TO_STORE_BLOOD_PRESSURE = 1
    AWAITING_BLOOD_PRESSURE_READING = 2


def current_state(input):
    session_attr = input.attributes_manager.session_attributes

    if ("state" in session_attr):
        raise Exception("TODO: Handle this properly...")

    return session_attr["state"]


def set_state(handler_input, newState):
    attr = handler_input.attributes_manager.persistent_attributes
    attr['state'] = newState
    handler_input.attributes_manager.session_attributes = attr


@sb.request_handler(can_handle_func=is_request_type("LaunchRequest"))
def launch_request_handler(handler_input):

    set_state(handler_input, State.DO_YOU_WANT_TO_STORE_BLOOD_PRESSURE)

    return handler_input.response_builder.speak("Would you like to record your blood pressure?").response


@sb.request_handler(can_handle_func=lambda input:
                    current_state(input) == State.DO_YOU_WANT_TO_STORE_BLOOD_PRESSURE and
                    is_intent_name("AMAZON.YesIntent")(input))
def store_blood_pressure_yes_handler(handler_input):

    set_state(handler_input, State.AWAITING_BLOOD_PRESSURE_READING)

    return handler_input.response_builder.speak("Please tell me your blood pressure?").response


@sb.request_handler(can_handle_func=lambda input:
                    current_state(input) == State.AWAITING_BLOOD_PRESSURE_READING and
                    is_intent_name("BloodPressureReading")(input))
def blood_pressure_reading_handler(handler_input):
    store_blood_pressure(handler_input)


@sb.request_handler(can_handle_func=is_intent_name("AMAZON.HelpIntent"))
def help_intent_handler(handler_input):
    logger.info("In HelpIntentHandler")
    handler_input.response_builder.speak("Boom Boom").ask("Please go again")
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=is_intent_name("StoreBloodPressure"))
def blood_pressure_intent_handler(handler_input):
    store_blood_pressure(handler_input)


def store_blood_pressure(handler_input):
    logger.info(f"StoreBloodPressure")
    response_builder = handler_input.response_builder

    print(handler_input.request_envelope.request)
    systolic_number = handler_input.request_envelope.request.intent.slots["systolic_number"].value
    diastolic_number = handler_input.request_envelope.request.intent.slots["diastolic_number"].value

    api_services = ApiServices()
    api_services.store_blood_pressure(systolic_number, diastolic_number)

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
