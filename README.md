# Alexa-Stack-Overflow
Alexa skill for Stack overflow

# Link to the Skill on Amazon Skill store

US - [Stack Overflow US skill Store](https://www.amazon.com/dp/B07HGW33GQ/ref=sr_1_2?s=digital-skills&ie=UTF8&qid=1537339798&sr=1-2&keywords=stack+overflow)<br />
India - [Stack Overflow India skill Store](https://www.amazon.in/s/ref=sr_nr_n_0?fst=as%3Aoff&rh=n%3A11928183031%2Cn%3A12113608031%2Ck%3Astack+overflow&keywords=stack+overflow&ie=UTF8&qid=1537338810&rnid=11928185031)<br />
UK - [Stack Overflow UK skill Store](https://www.amazon.co.uk/Yash-Stack-Overflow/dp/B07HGW33GQ/ref=sr_1_2?ie=UTF8&qid=1537683988&sr=8-2&keywords=stack+overflow)<br />
Australia - [Stack Overflow Australia skill Store](https://www.amazon.com.au/Yash-Stack-Overflow/dp/B07HGW33GQ/ref=sr_1_1?ie=UTF8&qid=1537684024&sr=8-1&keywords=stack+overflow)<br />
Canada - [Stack Overflow Canada skill Store](https://www.amazon.ca/Yash-Stack-Overflow/dp/B07HGW33GQ/ref=sr_1_1?ie=UTF8&qid=1537684055&sr=8-1&keywords=stack+overflow)

# Video-Demonstration
[Link to Youtube video](https://youtu.be/tuy70RlCJXg) 

# Getting Started
```python
# Clone the github repo
git clone https://github.com/mr-yamraj/Alexa-Stack-Overflow.git
cd Alexa-Stack-Overflow

#install all the dependencies
pip install requirements.txt

#run the function
python lambda_function.py <test-case-index>
Ex : python lambda_function.py 2 
# You can change the testcases by changing the index number 0 to 9 description of all the test cases is provided below
```

## Description of Test Cases

test_case[0] - Launch Request "Alexa, open stack overflow"
test_case[1] - Help Intent "Alexa, ask stack overflow help"
test_case[2] - Library Install request "Alexa, ask stack overflow how to install opencv in python"
test_case[3] - When Alexa ask to coinfirm the question and user responds "no"
test_case[4] - When Alexa ask to coinfirm the question and user responds "yes"
test_case[5] - When Alexa provide answer to the question and user responds "repeat"
test_case[6] - When user says yes to provide comments to the answer "yes"
test_case[7] - When Alexa asks user whether or not to provide second best answer to the question and user responds "yes"
test_case[8] - Error Intent "Alexa, ask stack overflow ehat is identation error in python"
test_case[9] - Comparision Intent "Alexa, ask stack overflow which is superior Python or C++"