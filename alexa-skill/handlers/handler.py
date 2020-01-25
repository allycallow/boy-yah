import logging
from ask_sdk_core.utils import is_intent_name
from ask_sdk_core.skill_builder import SkillBuilder

sb = SkillBuilder()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@sb.request_handler(can_handle_func=is_intent_name("AMAZON.HelpIntent"))
def help_intent_handler(handler_input):
    logger.info("In HelpIntentHandler")
    handler_input.response_builder.speak("Boom Boom").ask("Please go again")
    return handler_input.response_builder.response
