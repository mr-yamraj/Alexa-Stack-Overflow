def get_session_attributes(previous_intent = "", previous_intent_attributes = "", requested_value = "", previous_requested_value = "", questions_ids = [], question_now_id = 0, question_name = "", answers_ids = [], answer_now_id = 0, comments_ids = [], comment_now_id = 0,  complete_answer = [], complete_code = [], complete_code_now_id = 0):
    sessionAttributes = {}
    sessionAttributes["questions_ids"] = questions_ids
    sessionAttributes["question_now_id"] = question_now_id
    sessionAttributes["question_name"] = question_name
    sessionAttributes["answers_ids"] = answers_ids
    sessionAttributes["answer_now_id"] = answer_now_id
    sessionAttributes["comments_ids"] = comments_ids
    sessionAttributes["comment_now_id"] = comment_now_id
    sessionAttributes["previous_intent"] = previous_intent
    sessionAttributes["previous_intent_attributes"] = previous_intent_attributes
    sessionAttributes["complete_answer"] = complete_answer
    sessionAttributes["complete_code"] = complete_code
    sessionAttributes["complete_code_now_id"] = complete_code_now_id
    sessionAttributes["requested_value"] = requested_value
    sessionAttributes["previous_requested_value"] = previous_requested_value
    return sessionAttributes

def get_outputSpeech(outputSpeech_type, outputSpeech_text):
    outputSpeech = {}
    outputSpeech["type"] = outputSpeech_type
    outputSpeech["text"] = outputSpeech_text
    return outputSpeech

def get_card(card_type, card_title, card_content, card_text):
    card = {}
    card["type"] = card_type
    card["title"] = card_title
    card["content"] = card_content
    card["text"] = card_text
    return card

def get_repromt(repromt_outputSpeech_type, repromt_outputSpeech_text):
    reprompt = {}
    reprompt["outputSpeech"] = get_outputSpeech(repromt_outputSpeech_type, repromt_outputSpeech_text)
    return reprompt

def get_response(outputSpeech_text, outputSpeech_type = "PlainText", card_type = "Standard", card_title = "", card_content = "", card_text = "", repromt_outputSpeech_type = "PlainText", repromt_outputSpeech_text = "", shouldEndSession = True):
    response = {}
    response["outputSpeech"] = get_outputSpeech(outputSpeech_type, outputSpeech_text)
    if card_title != "":
        response["card"] = get_card(card_type, card_title, card_content, card_text)
    if repromt_outputSpeech_text != "":
        response["reprompt"] = get_repromt(repromt_outputSpeech_type, repromt_outputSpeech_text)
    response["shouldEndSession"] = shouldEndSession
    return response

def give_response(response, session_attributes = {}):
    lambda_response = {}
    lambda_response["version"] = "string"
    if session_attributes != {}:
        lambda_response["sessionAttributes"] = session_attributes
    lambda_response["response"] = response
    return lambda_response