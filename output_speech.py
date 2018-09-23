from alexa_response import get_session_attributes, get_response, give_response
from search import search_name, search_answer

def session_end_greetings():
    outputSpeech_text = "I hope you got your answer"
    return get_response(outputSpeech_text = outputSpeech_text), get_session_attributes()

def get_cancel_instructions():
    response, session_attributes = session_end_greetings()
    return give_response(response = response, session_attributes = session_attributes)

def get_helping_instructions():
    outputSpeech_text = "You can ask me any programming related query or any library install or remove instructions. For example, What is indentation error or how to install opencv in ubuntu or how to remove android studio"
    response = get_response(outputSpeech_text = outputSpeech_text, shouldEndSession = False)
    session_attributes = get_session_attributes()
    return give_response(response = response, session_attributes = session_attributes)

def no_correct_answer():
    outputSpeech_text = "Sorry no one has posted correct answer to this question"
    return get_response(outputSpeech_text = outputSpeech_text), get_session_attributes()

def no_questions():
    outputSpeech_text = "Sorry no one has posted this question"
    return get_response(outputSpeech_text = outputSpeech_text), get_session_attributes()

def no_more_questions():
    outputSpeech_text = "Sorry their are no more questions regarding this query"
    return get_response(outputSpeech_text = outputSpeech_text), get_session_attributes()

def next_related_question(session):
    outputSpeech_text = "Do you want me to go to next related question?"
    shouldEndSession = False
    repromt_outputSpeech_text = "Do you want me to go to next related question?"
    session_attributes = get_session_attributes(requested_value="next_question", questions_ids = session["attributes"]["questions_ids"], question_now_id = session["attributes"]["question_now_id"])
    response = get_response(outputSpeech_text = outputSpeech_text, repromt_outputSpeech_text = repromt_outputSpeech_text, shouldEndSession = shouldEndSession)
    return response, session_attributes

def next_related_answer(session):
    outputSpeech_text = "Do you want me to go to next answer to the question?"
    shouldEndSession = False
    repromt_outputSpeech_text = "Do you want me to go to next answer to the question?"
    session_attributes = get_session_attributes(requested_value = "give_answer", questions_ids = session["attributes"]["questions_ids"], question_now_id = session["attributes"]["question_now_id"], question_name = session["attributes"]["question_name"], answers_ids = session["attributes"]["answers_ids"], answer_now_id = session["attributes"]["answer_now_id"])
    response = get_response(outputSpeech_text = outputSpeech_text, repromt_outputSpeech_text = repromt_outputSpeech_text, shouldEndSession = shouldEndSession)
    return response, session_attributes

def next_question(questions_ids, id_number):
    answers_ids, question_now_id_id, question_name, question_now_id = search_name(questions_ids, id_number)
    if answers_ids != 0:
        outputSpeech_text = "Are you looking for " + question_name
        shouldEndSession = False
        repromt_outputSpeech_text = "Please answer yes or no or repeat"
        session_attributes = get_session_attributes(requested_value = "give_answer", previous_requested_value = "next_question", questions_ids = questions_ids, question_now_id = question_now_id, question_name = question_name, answers_ids=answers_ids)
        response = get_response(outputSpeech_text = outputSpeech_text,  repromt_outputSpeech_text=repromt_outputSpeech_text, shouldEndSession = shouldEndSession)
        return response, session_attributes
    else:
        return no_correct_answer()

def required_response(session):
    if session["attributes"]["previous_requested_value"] != "":
        outputSpeech_text = "Please provide your response in yes, no or repeat only"
    else:
        outputSpeech_text = "Please provide your response in yes or no only"
    shouldEndSession = False
    session_attributes = session["attributes"]
    response = get_response(outputSpeech_text = outputSpeech_text, repromt_outputSpeech_text = outputSpeech_text, shouldEndSession = shouldEndSession)
    return response, session_attributes

def give_answer(session, is_repeat = False):
    if is_repeat == True:
        answer = session["attributes"]["complete_answer"]
        session["attributes"]["answer_now_id"] = session["attributes"]["answer_now_id"] - 1
    else:
        answer = search_answer(session["attributes"]["questions_ids"][session["attributes"]["question_now_id"] - 1], session["attributes"]["answers_ids"], session["attributes"]["answer_now_id"])
    if (answer["comment"] != ""):
        outputSpeech_text = answer["answer_text"] + " or do you want me to repeat the answer"
        shouldEndSession = False
        repromt_outputSpeech_text = "Please answer yes or no to get comments or say repeat to repeat the answer again."
        session_attributes = get_session_attributes(requested_value = "give_comment", previous_requested_value = "give_answer", questions_ids = session["attributes"]["questions_ids"], question_now_id = session["attributes"]["question_now_id"], question_name = session["attributes"]["question_name"], answers_ids = session["attributes"]["answers_ids"], answer_now_id = session["attributes"]["answer_now_id"] + 1, complete_answer = answer)
    else:
        outputSpeech_text = answer["answer_text"]
        if session["attributes"]["answer_now_id"] == len(session["attributes"]["answers_ids"]):
            if session["attributes"]["question_now_id"] < len(session["attributes"]["questions_ids"]):
                outputSpeech_text = outputSpeech_text + " Do you want me to go to next related question? or do you want me to repeat the answer?"
                shouldEndSession = False
                repromt_outputSpeech_text = "Please answer yes or no to go to next related question or say repeat to repeat the answer again."
                session_attributes = get_session_attributes(requested_value = "next_question", previous_requested_value = "give_answer", questions_ids = session["attributes"]["questions_ids"], question_now_id = session["attributes"]["question_now_id"], question_name = session["attributes"]["question_name"], complete_answer = answer)
            else:
                shouldEndSession = True
                repromt_outputSpeech_text = ""
                session_attributes = get_session_attributes()
        else:
            outputSpeech_text = outputSpeech_text + " Do you want me to go to next answer to the question? or do you want me to repeat the answer?"
            shouldEndSession = False
            repromt_outputSpeech_text = "Please answer yes or no to go to next answer or say repeat to repeat the answer again."
            session_attributes = get_session_attributes(requested_value = "give_answer", previous_requested_value = "give_answer", questions_ids = session["attributes"]["questions_ids"], question_now_id = session["attributes"]["question_now_id"], question_name = session["attributes"]["question_name"], answers_ids = session["attributes"]["answers_ids"], answer_now_id = session["attributes"]["answer_now_id"] + 1, complete_answer = answer)
    response = get_response(outputSpeech_text = outputSpeech_text, card_title = session["attributes"]["question_name"], card_content = "code", card_text = answer["card"], shouldEndSession = shouldEndSession, repromt_outputSpeech_text = repromt_outputSpeech_text)
    return response, session_attributes

def give_comment(session):
    outputSpeech_text = session["attributes"]["complete_answer"]["comment"]
    if session["attributes"]["answer_now_id"] == len(session["attributes"]["answers_ids"]):
        if session["attributes"]["question_now_id"] < len(session["attributes"]["questions_ids"]):
            outputSpeech_text = outputSpeech_text + " Do you want me to go to next related question? or do you want me to repeat the comments?"
            shouldEndSession = False
            repromt_outputSpeech_text = "Please answer yes or no to go to next related question or say repeat to repeat the comments again."
            session_attributes = get_session_attributes(requested_value = "next_question", previous_requested_value = "give_comment", questions_ids = session["attributes"]["questions_ids"], question_now_id = session["attributes"]["question_now_id"], question_name = session["attributes"]["question_name"], answers_ids = session["attributes"]["answers_ids"], complete_answer = session["attributes"]["complete_answer"])
        else:
            shouldEndSession = True
            session_attributes = get_session_attributes()
    else:
        outputSpeech_text = outputSpeech_text + " Do you want me to go to next answer to the question? or do you want me to repeat the comment?"
        shouldEndSession = False
        repromt_outputSpeech_text = "Please answer yes or no to go to next answer or say repeat to repeat the comment again."
        session_attributes = get_session_attributes(requested_value = "give_answer", previous_requested_value = "give_comment", questions_ids = session["attributes"]["questions_ids"], question_now_id = session["attributes"]["question_now_id"], question_name = session["attributes"]["question_name"], answers_ids = session["attributes"]["answers_ids"], answer_now_id = session["attributes"]["answer_now_id"], complete_answer = session["attributes"]["complete_answer"])
    response = get_response(outputSpeech_text = outputSpeech_text, shouldEndSession = shouldEndSession, repromt_outputSpeech_text = repromt_outputSpeech_text)    
    return response, session_attributes

def repeat_previous(session):
    if session["attributes"]["previous_requested_value"] != "":
        if session["attributes"]["previous_requested_value"] == "next_question":
            outputSpeech_text = session["attributes"]["question_name"]
            shouldEndSession = False
            repromt_outputSpeech_text = "Please answer yes or no or repeat"
            session_attributes = session["attributes"]
            response = get_response(outputSpeech_text = outputSpeech_text,  repromt_outputSpeech_text=repromt_outputSpeech_text, shouldEndSession = shouldEndSession)
            return response, session_attributes
        elif session["attributes"]["previous_requested_value"] == "give_answer":
            return give_answer(session = session, is_repeat = True)
        elif session["attributes"]["previous_requested_value"] == "give_comment":
            return give_comment(session)
    else:
        return required_response(session)