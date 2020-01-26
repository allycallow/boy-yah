import logging
import boto3

from ask_sdk_core.utils import is_intent_name, is_request_type
from ask_sdk_core.skill_builder import CustomSkillBuilder
from ask_sdk_model.ui import SimpleCard
from utils.api_services import ApiServices
from utils.email_services import EmailServices
from enum import Enum

bucket_name = os.environ.get('ALEXA_STATE_BUCKET')
s3_client = boto3.client('s3', config=boto3.session.Config(signature_version='s3v4',s3={'addressing_style': 'path'}))
s3_adapter = S3Adapter(bucket_name=bucket_name, path_prefix="Media", s3_client=s3_client)
sb = CustomSkillBuilder(persistence_adapter=s3_adapter)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class State(Enum):
    DO_YOU_WANT_TO_STORE_BLOOD_PRESSURE = 1
    AWAITING_BLOOD_PRESSURE_READING = 2
    DO_YOU_WANT_TO_STORE_PEAK_FLOW = 3
    AWAITING_PEAK_FLOW_READING = 4


def current_state(input):
    session_attr = input.attributes_manager.session_attributes

    if ("state" in session_attr):
        raise Exception("TODO: Handle this properly...")

    return session_attr["state"]


def set_state(input, newState):
    attr = input.attributes_manager.persistent_attributes
    attr['state'] = newState
    input.attributes_manager.session_attributes = attr


@sb.request_handler(can_handle_func=is_request_type("LaunchRequest"))
def launch_request_handler(input):

    set_state(input, State.DO_YOU_WANT_TO_STORE_BLOOD_PRESSURE)

    return input.response_builder.speak("Would you like to record your blood pressure?").response


@sb.request_handler(can_handle_func=lambda input:
                    current_state(input) == State.DO_YOU_WANT_TO_STORE_BLOOD_PRESSURE and
                    is_intent_name("AMAZON.YesIntent")(input))
def store_blood_pressure_yes_handler(input):
    set_state(input, State.AWAITING_BLOOD_PRESSURE_READING)
    return input.response_builder.speak("Please tell me your blood pressure").response


@sb.request_handler(can_handle_func=lambda input:
                    current_state(input) == State.AWAITING_BLOOD_PRESSURE_READING and
                    is_intent_name("BloodPressureReading")(input))
def blood_pressure_reading_handler(input):
    store_blood_pressure(input)
    return ask_do_you_want_to_store_peak_flow(input)
    

def ask_do_you_want_to_store_peak_flow(input):
    set_state(input, State.AWAITING_PEAK_FLOW_READING)
    return input.response_builder.speak("Would you like to record your peak flow?").response


@sb.request_handler(can_handle_func=lambda input:
                    current_state(input) == State.DO_YOU_WANT_TO_STORE_PEAK_FLOW and
                    is_intent_name("AMAZON.YesIntent")(input))
def store_peak_flow_yes_handler(input):
    set_state(input, State.DO_YOU_WANT_TO_STORE_PEAK_FLOW)
    return input.response_builder.speak("Please tell me your peak flow rate").response


@sb.request_handler(can_handle_func=lambda input:
                    current_state(input) == State.AWAITING_PEAK_FLOW_READING and
                    is_intent_name("PeakFlowRateReading")(input))
def blood_pressure_reading_handler(input):
    store_peak_flow(input)


@sb.request_handler(can_handle_func=is_intent_name("AMAZON.HelpIntent"))
def help_intent_handler(input):
    logger.info("In HelpIntentHandler")
    input.response_builder.speak("Boom Boom").ask("Please go again")
    return input.response_builder.response


@sb.request_handler(can_handle_func=is_intent_name("StoreBloodPressure"))
def blood_pressure_intent_handler(input):
    store_blood_pressure(input)


def store_blood_pressure(input):
    logger.info(f"StoreBloodPressure")
    response_builder = input.response_builder

    print(input.request_envelope.request)
    systolic_number = input.request_envelope.request.intent.slots["systolic_number"].value
    diastolic_number = input.request_envelope.request.intent.slots["diastolic_number"].value

    api_services = ApiServices()
    api_services.store_blood_pressure(systolic_number, diastolic_number)

    speech_text = f"working {systolic_number} {diastolic_number}"

    return response_builder.speak(speech_text).set_should_end_session(False).response


@sb.request_handler(can_handle_func=is_intent_name("StorePeakFlowRate"))
def peak_flow_rate_intent_handler(input):
    logger.info(f"StorePeakFlowRate")
    store_peak_flow(input)

def store_peak_flow(input):
    response_builder = input.response_builder

    print(input.request_envelope.request)
    peak_flow_rate = input.request_envelope.request.intent.slots["peak_flow_rate"].value

    api_services = ApiServices()
    api_services.store_peak_flow_rate(peak_flow_rate)

    speech_text = f"working {peak_flow_rate}"

    return response_builder.speak(speech_text).set_should_end_session(False).response


@sb.exception_handler(can_handle_func=lambda i, e: True)
def all_exception_handler(input, exception):
    """Catch all exception handler, log exception and
    respond with custom message.
    """
    # type: (HandlerInput, Exception) -> Response
    logger.error(exception, exc_info=True)

    speech = "Sorry, there was some problem. Please try again!!"
    input.response_builder.speak(speech).ask(speech)

    return input.response_builder.response


@sb.request_handler(can_handle_func=is_intent_name("SendToDoctor"))
def send_to_doctor_intent_handler(input):
    logger.info(f"SendToDoctor")
    response_builder = input.response_builder

    email_services = EmailServices()
    email_services.send_mail()

    speech_text = f"Your doctor has now been sent your records."

    return response_builder.speak(speech_text).set_should_end_session(False).response


handler = sb.lambda_handler()
