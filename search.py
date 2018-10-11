import re
import json
import requests
from bs4 import BeautifulSoup
from urlparse import urlparse
from sites import stackexchange_sites
from search_stackexchange import search_name_stackexchange, search_answer_stackexchange

def search_name(questions_urls, id_number):
    for i in range(id_number, len(questions_urls)):
        url = questions_urls[i]
        parsed_uri = urlparse(url)
        domain = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
        if (domain in stackexchange_sites):
            print domain
            answer_id_list, question_name = search_name_stackexchange(questions_urls[i])
            if answer_id_list != 0:
                return answer_id_list, questions_urls[i], question_name, i+1
    return 0, 0, "none", 0

def search_questions(query):
    print query
    query = query.replace(" ", "%20")
    url = "http://www.bing.com/search?count=50&q=" + query
    r  = requests.get(url)
    website = r.text
    soup = BeautifulSoup(website)
    body = soup.find("body")
    content_url = body.find("div", {"id": "b_content"})
    results_url = content_url.find("ol", {"id": "b_results"})
    results = results_url.find_all("li", {"class": "b_algo"})
    urls = []
    questions = []
    for result in results:
        parsed_uri = urlparse(result.find('a')['href'])
        domain = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
        if (domain in stackexchange_sites):
            urls.append(result.find('a')['href'])
            # print result.find('a')['href']
            try:
                questions.append(result.find('a')['href'])
                # questions.append(re.search(r'[0-9]+', re.search(r'questions/[0-9]+/', result.find('a')['href']).group()).group())
            except:
                a = 1
    return questions

def search_answer(question_url, answer_ids, id_number):
    parsed_uri = urlparse(question_url)
    domain = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
    if (domain in stackexchange_sites):
        answer = search_answer_stackexchange(question_url, answer_ids, id_number)
        return answer