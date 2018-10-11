from alexa_response import get_session_attributes, get_response, give_response
from search import search_name, search_questions, search_answer
from output_speech import session_end_greetings, get_cancel_instructions, get_helping_instructions, no_correct_answer, no_questions, no_more_questions, next_related_question, next_related_answer, next_question, required_response, give_answer, give_comment, repeat_previous
from testcase import get_testcase
import sys

def lambda_handler(event, context):
    # print event
    if event["session"]["new"]:
        on_session_started(event["session"])
    if event["request"]["type"] == "LaunchRequest":
        return on_launch(event["request"], event["session"])
    elif event["request"]["type"] == "IntentRequest":
        return on_intent(event["request"], event["session"])
    elif event["request"]["type"] == "SessionEndedRequest":
        return on_session_ended(event["request"], event["session"])

def on_session_started(session):
    print "Starting new session."

def on_launch(launch_request, session):
    return get_welcome_response()

def get_welcome_response():
    response_text = "Hi! I am from stack overflow, I can help you with any programming query!"
    # card_title = "Title of the card"
    # card_content = "Content of a simple card"
    # card_text = "Text content for a standard card"
    response = get_response(outputSpeech_text = response_text, shouldEndSession = False)
    session_attributes = get_session_attributes()
    return give_response(response = response, session_attributes = session_attributes)

def on_intent(intent_request, session):
    intent = intent_request["intent"]
    intent_name = intent_request["intent"]["name"]

    if intent_name == "library_install_Intent":
        return get_install_instructions(intent_request, session)
    elif intent_name == "library_remove_Intent":
        return get_remove_instructions(intent_request, session)
    elif intent_name == "Error_Intent":
        return get_error_instructions(intent_request, session)
    elif intent_name == "Help_Intent":
        return get_help_instructions(intent_request, session)
    elif intent_name == "Comparision_Intent":
        return get_comparision_instructions(intent_request, session)
    elif intent_name == "AnswerIntent":
        return add_ans(intent_request, session)
    elif intent_name == "AMAZON.CancelIntent":
        return get_cancel_instructions()
    elif intent_name == "AMAZON.StopIntent":
        return get_cancel_instructions()
    elif intent_name == "AMAZON.HelpIntent":
        return get_helping_instructions()


def add_ans(intent_request, session):
    if session["attributes"]["previous_intent"] == "library_install_Intent":
        if session["attributes"]["requested_value"] in ["library_name", "operating_system", "answer_response"]:
            return get_install_instructions(intent_request = intent_request, session = session, answer_intent = True)
    elif session["attributes"]["previous_intent"] == "library_remove_Intent":
        if session["attributes"]["requested_value"] in ["library_name", "operating_system", "answer_response"]:
            return get_remove_instructions(intent_request = intent_request, session = session, answer_intent = True)
    elif session["attributes"]["previous_intent"] == "Error_Intent":
        if session["attributes"]["requested_value"] in ["error_name", "answer_response"]:
            return get_error_instructions(intent_request = intent_request, session = session, answer_intent = True)
    elif session["attributes"]["previous_intent"] == "Help_Intent":
        if session["attributes"]["requested_value"] in ["query_name", "answer_response"]:
            return get_help_instructions(intent_request = intent_request, session = session, answer_intent = True)
    elif session["attributes"]["previous_intent"] == "Comparision_Intent":
        if session["attributes"]["requested_value"] in ["Comparision_a", "Comparision_b", "answer_response"]:
            return get_comparision_instructions(intent_request = intent_request, session = session, answer_intent = True)
    else:
        return all_response(intent_request = intent_request, session = session)
        
def get_intent_attributes(intent_request, session, answer_intent):
    intent_attributes = {}
    if answer_intent == False:
        try:
            intent_attributes["library_name"] = intent_request["intent"]["slots"]["library_name"]["value"]
        except:
            intent_attributes["library_name"] = "NONE"
        try:
            intent_attributes["operating_system"] = intent_request["intent"]["slots"]["operating_system"]["value"]
        except:
            intent_attributes["operating_system"] = "NONE"
        try:
            intent_attributes["software_management_library"] = intent_request["intent"]["slots"]["software_management_library"]["value"]
        except:
            intent_attributes["software_management_library"] = "NONE"
        try:
            intent_attributes["error_name"] = intent_request["intent"]["slots"]["error_name"]["value"]
        except:
            intent_attributes["error_name"] = "NONE"
        try:
            intent_attributes["query_name"] = intent_request["intent"]["slots"]["query_name"]["value"]
        except:
            intent_attributes["query_name"] = "NONE"
        try:
            intent_attributes["Comparision_a"] = intent_request["intent"]["slots"]["Comparision_a"]["value"]
        except:
            intent_attributes["Comparision_a"] = "NONE"
        try:
            intent_attributes["Comparision_b"] = intent_request["intent"]["slots"]["Comparision_b"]["value"]
        except:
            intent_attributes["Comparision_b"] = "NONE"
    elif answer_intent == True:
        intent_attributes["library_name"] = session["attributes"]["previous_intent_attributes"]["library_name"]
        intent_attributes["operating_system"] = session["attributes"]["previous_intent_attributes"]["operating_system"]
        intent_attributes["software_management_library"] = session["attributes"]["previous_intent_attributes"]["software_management_library"]
        intent_attributes["error_name"] = session["attributes"]["previous_intent_attributes"]["error_name"]
        intent_attributes["query_name"] = session["attributes"]["previous_intent_attributes"]["query_name"]
        intent_attributes["Comparision_a"] = session["attributes"]["previous_intent_attributes"]["Comparision_a"]
        intent_attributes["Comparision_b"] = session["attributes"]["previous_intent_attributes"]["Comparision_b"]
        intent_attributes[session["attributes"]["requested_value"]] = intent_request["intent"]["slots"]["answer"]["value"]
    return intent_attributes

def all_response(intent_request, query = "", session = ""):
    if session["new"] == False:
        if (session["attributes"]["requested_value"] in ["next_question", "give_comment", "next_answer", "give_answer"]):
            if intent_request["intent"]["slots"]["answer"]["value"] not in ["yes", "no", "repeat"]:
                response, session_attributes = required_response(session)
    if session["new"] == True:
        questions_urls= search_questions(query) # urls, domains
        if len(questions_urls) > 0:
            response, session_attributes = next_question(questions_urls, 0)
        else:
            response, session_attributes = no_questions()
    elif (session["attributes"]["requested_value"] not in ["next_question", "give_comment", "next_answer", "give_answer"]):
        print "hello"
        questions_urls = search_questions(query) # urls, domains
        if len(questions_urls) > 0:
            response, session_attributes = next_question(questions_urls, 0)
        else:
            response, session_attributes = no_questions()
    elif intent_request["intent"]["slots"]["answer"]["value"] == "repeat":
        response, session_attributes = repeat_previous(session)
    elif session["attributes"]["requested_value"] == "give_answer":
        if intent_request["intent"]["slots"]["answer"]["value"] == "no":
            if session["attributes"]["previous_requested_value"] == "next_question":
                if session["attributes"]["question_now_id"] < len(session["attributes"]["questions_urls"]):
                    response, session_attributes = next_question(session["attributes"]["questions_urls"], session["attributes"]["question_now_id"])
                else:
                    response, session_attributes = no_more_questions()
            else:
                response, session_attributes = session_end_greetings()
        elif intent_request["intent"]["slots"]["answer"]["value"] == "yes":
            response, session_attributes = give_answer(session)

    elif session["attributes"]["requested_value"] == "give_comment":
        if intent_request["intent"]["slots"]["answer"]["value"] == "no":
            if session["attributes"]["answer_now_id"] == len(session["attributes"]["answers_ids"]):
                if session["attributes"]["question_now_id"] < len(session["attributes"]["questions_urls"]):
                    response, session_attributes = next_related_question(session)
                else:
                    response, session_attributes = session_end_greetings()
            else:
                response, session_attributes = next_related_answer(session)
        elif intent_request["intent"]["slots"]["answer"]["value"] == "yes":
            response, session_attributes = give_comment(session)

    elif session["attributes"]["requested_value"] == "next_question":
        if intent_request["intent"]["slots"]["answer"]["value"] == "no":
            response, session_attributes = session_end_greetings()
        elif intent_request["intent"]["slots"]["answer"]["value"] == "yes":
            if session["attributes"]["question_now_id"] < len(session["attributes"]["questions_urls"]):
                response, session_attributes = next_question(session["attributes"]["questions_urls"], session["attributes"]["question_now_id"])
            else:
                response, session_attributes = no_more_questions()
        else:
            response, session_attributes = session_end_greetings()
    return give_response(response = response, session_attributes = session_attributes)

def get_install_instructions(intent_request, session, answer_intent = False):
    # print "yesy"
    intent_attributes = get_intent_attributes(intent_request, session, answer_intent)
    if intent_attributes["library_name"] == "NONE":
        outputSpeech_text = "Which library do you want to install."
        repromt_outputSpeech_text="Please tell which library do you want to install."
        session_attributes = get_session_attributes(previous_intent = "library_install_Intent", previous_intent_attributes = intent_attributes, requested_value = "library_name")
        response = get_response(outputSpeech_text = outputSpeech_text, repromt_outputSpeech_text=repromt_outputSpeech_text, shouldEndSession = False)
    elif intent_attributes["operating_system"] == "NONE":
        outputSpeech_text = "In which operating system do you like to install " + intent_attributes["library_name"]
        repromt_outputSpeech_text = "Please tell in which operating system do you like to install " + intent_attributes["library_name"]
        session_attributes = get_session_attributes(previous_intent = "library_install_Intent", previous_intent_attributes = intent_attributes, requested_value = "operating_system")
        response = get_response(outputSpeech_text = outputSpeech_text,  repromt_outputSpeech_text=repromt_outputSpeech_text, shouldEndSession = False)
    else:
        query = "how to install " + intent_attributes["library_name"] + " in " + intent_attributes["operating_system"]
        # query = "superuser opencv install"
        return all_response(query = query, session = session, intent_request = intent_request)
    return give_response(response = response, session_attributes = session_attributes)

    
def get_remove_instructions(intent_request, session, answer_intent = False):
    print "yesy"
    intent_attributes = get_intent_attributes(intent_request, session, answer_intent)
    if intent_attributes["library_name"] == "NONE":
        outputSpeech_text = "Which library do you want to remove."
        repromt_outputSpeech_text="Please tell which library do you want to remove."
        session_attributes = get_session_attributes(previous_intent = "library_remove_Intent", previous_intent_attributes = intent_attributes, requested_value = "library_name")
        response = get_response(outputSpeech_text = outputSpeech_text, repromt_outputSpeech_text=repromt_outputSpeech_text, shouldEndSession = False)
    elif intent_attributes["operating_system"] == "NONE":
        outputSpeech_text = "From which operating system do you like to remove " + intent_attributes["library_name"]
        repromt_outputSpeech_text = "Please tell from which operating system do you like to remove " + intent_attributes["library_name"]
        session_attributes = get_session_attributes(previous_intent = "library_remove_Intent", previous_intent_attributes = intent_attributes, requested_value = "operating_system")
        response = get_response(outputSpeech_text = outputSpeech_text,  repromt_outputSpeech_text=repromt_outputSpeech_text, shouldEndSession = False)
    else:
        query = "how to remove " + intent_attributes["library_name"] + " from " + intent_attributes["operating_system"]
        return all_response(query = query, session = session, intent_request = intent_request)
    return give_response(response = response, session_attributes = session_attributes)

def get_error_instructions(intent_request, session, answer_intent = False):
    # print "yesy"
    intent_attributes = get_intent_attributes(intent_request, session, answer_intent)
    if intent_attributes["error_name"] == "NONE":
        outputSpeech_text = "What is your error."
        repromt_outputSpeech_text="Please tell what is the error you are facing."
        session_attributes = get_session_attributes(previous_intent = "Error_Intent", previous_intent_attributes = intent_attributes, requested_value = "error_name")
        response = get_response(outputSpeech_text = outputSpeech_text, repromt_outputSpeech_text=repromt_outputSpeech_text, shouldEndSession = False)
    else:
        query = "error " + intent_attributes["error_name"]
        return all_response(query = query, session = session, intent_request = intent_request)
    return give_response(response = response, session_attributes = session_attributes)

def get_help_instructions(intent_request, session, answer_intent = False):
    # print "yesy"
    intent_attributes = get_intent_attributes(intent_request, session, answer_intent)
    if intent_attributes["query_name"] == "NONE":
        outputSpeech_text = "What is your query."
        repromt_outputSpeech_text="Please tell me your query."
        session_attributes = get_session_attributes(previous_intent = "Help_Intent", previous_intent_attributes = intent_attributes, requested_value = "query_name")
        response = get_response(outputSpeech_text = outputSpeech_text, repromt_outputSpeech_text=repromt_outputSpeech_text, shouldEndSession = False)
    else:
        query = "help " + intent_attributes["query_name"]
        return all_response(query = query, session = session, intent_request = intent_request)
    return give_response(response = response, session_attributes = session_attributes)

def get_comparision_instructions(intent_request, session, answer_intent = False):
    # print "yesy"
    intent_attributes = get_intent_attributes(intent_request, session, answer_intent)
    if (intent_attributes["Comparision_a"] == "NONE") & (intent_attributes["Comparision_b"] != "NONE"):
        outputSpeech_text = "With what do you want to compare " + intent_attributes["Comparision_b"]
        repromt_outputSpeech_text="Please tell me with what do you want to compare " + intent_attributes["Comparision_b"]
        session_attributes = get_session_attributes(previous_intent = "Comparision_Intent", previous_intent_attributes = intent_attributes, requested_value = "Comparision_a")
        response = get_response(outputSpeech_text = outputSpeech_text, repromt_outputSpeech_text=repromt_outputSpeech_text, shouldEndSession = False)
    elif (intent_attributes["Comparision_a"] != "NONE") & (intent_attributes["Comparision_b"] == "NONE"):
        outputSpeech_text = "With what do you want to compare " + intent_attributes["Comparision_a"]
        repromt_outputSpeech_text="Please tell me with what do you want to compare " + intent_attributes["Comparision_a"]
        session_attributes = get_session_attributes(previous_intent = "Comparision_Intent", previous_intent_attributes = intent_attributes, requested_value = "Comparision_b")
        response = get_response(outputSpeech_text = outputSpeech_text, repromt_outputSpeech_text=repromt_outputSpeech_text, shouldEndSession = False)
    elif (intent_attributes["Comparision_a"] == "NONE") & (intent_attributes["Comparision_b"] == "NONE"):
        outputSpeech_text = "What do you want to compare."
        session_attributes = get_session_attributes(previous_intent = "Comparision_Intent", previous_intent_attributes = intent_attributes, requested_value = "Comparision_a")
        response = get_response(outputSpeech_text = outputSpeech_text, shouldEndSession = False)
    else:
        query = "xwhich is better " + intent_attributes["Comparision_a"] + " or " + intent_attributes["Comparision_b"]
        return all_response(query = query, session = session, intent_request = intent_request)
    return give_response(response = response, session_attributes = session_attributes)

def on_session_ended(session_ended_request, session):
    print "Ending session."
    # Cleanup goes here...
if __name__ == "__main__":
    test_case = get_testcase()
    # index = sys.argv[1]
    # index = 5
    # print lambda_handler(test_case[int(index)], {})
    try:
        index = sys.argv[1]
        if((int(index) > 9)|(int(index) < 0)):
            print "Please provide test case index between 0-9"
            print '0 - Launch Request "Alexa, open stack overflow"'
            print '1 - Help Intent "Alexa, ask stack overflow help"'
            print '2 - Library Install request "Alexa, ask stack overflow how to install opencv in python"'
            print '3 - When Alexa ask to coinfirm the question and user responds "no"'
            print '4 - When Alexa ask to coinfirm the question and user responds "yes"'
            print '5 - When Alexa provide answer to the question and user responds "repeat"'
            print '6 - When user says yes to provide comments to the answer "yes"'
            print '7 - When Alexa asks user whether or not to provide second best answer to the question and user responds "yes"'
            print '8 - Error Intent "Alexa ask stack overflow what is identation error in python"'
            print '9 - Comparision Intent "Alexa ask stack overflow which is superior Python or C++"'
        else:
            print lambda_handler(test_case[int(index)], {})
    except:
        print "Please provide test case number for ex : python lambda_function.py <test-case-index>"
        print '0 - Launch Request "Alexa, open stack overflow"'
        print '1 - Help Intent "Alexa, ask stack overflow help"'
        print '2 - Library Install request "Alexa, ask stack overflow how to install opencv in python"'
        print '3 - When Alexa ask to coinfirm the question and user responds "no"'
        print '4 - When Alexa ask to coinfirm the question and user responds "yes"'
        print '5 - When Alexa provide answer to the question and user responds "repeat"'
        print '6 - When user says yes to provide comments to the answer "yes"'
        print '7 - When Alexa asks user whether or not to provide second best answer to the question and user responds "yes"'
        print '8 - Error Intent "Alexa, ask stack overflow ehat is identation error in python"'
        print '9 - Comparision Intent "Alexa, ask stack overflow which is superior Python or C++"'