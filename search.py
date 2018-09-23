import re
import json
import requests
from bs4 import BeautifulSoup
from urlparse import urlparse

def search_name(questions_ids, id_number):
    for i in range(id_number, len(questions_ids)):
        url = "https://api.stackexchange.com/2.2/questions/" + questions_ids[i] + "/answers?order=desc&sort=activity&site=stackoverflow"
        r  = requests.get(url)
        # print r.text
        x = json.loads(str(r.text))
        if (len(x["items"]) > 0):
            answer_id_list = []
            temp_id_list = []
            answer_upvotes = []
            for answer in x["items"]:
                if answer["is_accepted"] == True:
                    answer_id_list.append(answer["answer_id"])
                else:
                    temp_id_list.append(answer["answer_id"])
                    answer_upvotes.append(answer["score"])
#             print temp_id_list
#             print answer_upvotes
            temp = [x for _,x in sorted(zip(answer_upvotes,temp_id_list), reverse=True)]
#             print temp
            answer_id_list = answer_id_list + temp
#             print answer_id_list
            url = "https://api.stackexchange.com/2.2/questions/" + questions_ids[i] + "?order=desc&sort=activity&site=stackoverflow"
            r = requests.get(url)
            x = json.loads(str(r.text))
            question_name = x["items"][0]["title"]
            return answer_id_list, questions_ids[i], question_name, i+1
#         for answer in x["items"]:
#             print answer
#             if answer["is_accepted"] == True:
#                 url = "https://api.stackexchange.com/2.2/questions/" + questions_ids[i] + "?order=desc&sort=activity&site=stackoverflow"
#                 r = requests.get(url)
#                 x = json.loads(str(r.text))
#                 question_name = x["items"][0]["title"]
#                 return answer["answer_id"], questions_ids[i], question_name, i+1
    return 0, 0, "none", 0

def search_questions(query):
    print query
    query = query.replace(" ", "%20")
    url = "http://www.bing.com/search?count=50&q=" + query
    r  = requests.get(url)
    website = r.text
    soup = BeautifulSoup(website)
    # print soup.text
    body = soup.find("body")
    content_url = body.find("div", {"id": "b_content"})
    results_url = content_url.find("ol", {"id": "b_results"})
    results = results_url.find_all("li", {"class": "b_algo"})
    urls = []
    questions = []
    # print results
    for result in results:
        # print result.find('a')['href']
        parsed_uri = urlparse(result.find('a')['href'])
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        # print domain
        if (domain[-18:] == 'stackoverflow.com/')|(domain[-18:] == 'stackexchange.com/'):
            urls.append(result.find('a')['href'])
            # print result.find('a')['href']
            try:
                questions.append(re.search(r'[0-9]+', re.search(r'questions/[0-9]+/', result.find('a')['href']).group()).group())
                # print result.find('a')['href']
            except:
                a = 1
            # print questions
    return questions
# 	text = get_question_title(questions)
# 	get_answers_id(questions)

def search_answer(question_id, answer_ids, id_number):
    url = "https://api.stackexchange.com/2.2/questions/" + question_id + "?order=desc&sort=activity&site=stackoverflow"
    r = requests.get(url)
    x = json.loads(str(r.text))
    question_url = x["items"][0]["link"]
    owner_id = x["items"][0]["owner"]["user_id"]
    # print question_url
    r = requests.get(question_url)
    data = r.text
    soup = BeautifulSoup(data)
    temp_answers = soup.find(id = "answers")
    temp_answer = temp_answers.find(id = "answer-" + str(answer_ids[id_number]))
    answer_text = temp_answer.find(class_="post-text")
    comment_text = temp_answer.find(id="comments-" + str(answer_ids[id_number]))
    comments = comment_text.findAll('li')
    comment_text_list = []
    comment_by_list = []
    Comment_string = ""
    # print comments[1]
    for comment in comments:
        temp_comment = comment.find(class_="comment-copy")
        temp_text = temp_comment.get_text()
        id_1 = comment.find('a')
        temp_id = id_1["href"].split('/')[2]
        if str(owner_id) == temp_id:
            Comment_string = Comment_string + " Owner of the question " + "said " + temp_text + "."
        else:
            Comment_string = Comment_string + " A person " + "said " + temp_text + "."
    answer = {}
    codes = answer_text.findAll('pre')
    code_string = ""
    for code in codes:
        code = code.get_text()
        code_string = code_string + code
    if code_string != '':
        answer["card"] = answer_text.get_text() + "\nCode : \n" + code_string
        if Comment_string != "":
                answer["answer_text"] = answer_text.get_text() + " For code and answer please refer to the response card in your alexa app. Do you want to hear the comments to this answer."
                answer["comment"] = Comment_string
        else:
            answer["comment"] = Comment_string
            answer["answer_text"] = answer_text.get_text() + " For code and answer please refer to the response card in your alexa app."
    else:
        answer["card"] = answer_text.get_text()
        if Comment_string != "":
                answer["answer_text"] = answer_text.get_text() + " For code and answer please refer to the response card in your alexa app. Do you want to hear the comments to this answer."
                answer["comment"] = Comment_string
        else:
            answer["comment"] = Comment_string
            answer["answer_text"] = answer_text.get_text() + " For code and answer please refer to the response card in your alexa app."
    return answer