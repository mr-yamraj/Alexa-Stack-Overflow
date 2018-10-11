def get_testcase():
	temp_data = [{
		"version": "1.0",
		"session": {
			"new": True
					},
		"request": {
			"type": "LaunchRequest",
			"shouldLinkResultBeReturned": False
		}
	},
	{
		"version": "1.0",
		"session": {
			"new": True
					},
		"request": {
			"type": "IntentRequest",
			"intent": {
				"name": "AMAZON.HelpIntent",
				"confirmationStatus": "NONE"
			}
		}
	},
	{
	"version": "1.0",
	"session": {
		"new": True
	},
	"request": {
		"type": "IntentRequest",
		"intent": {
			"name": "library_install_Intent",
			"confirmationStatus": "NONE",
			"slots": {
				"library_name": {
					"name": "library_name",
					"value": "opencv",
					"resolutions": {
						"resolutionsPerAuthority": [
							{
								"authority": "amzn1.erauthority.echosdk.amzn1.ask.skill.79c68afc19b14e1aa7286481798feabf.library_name",
								"status": {
									"code": "ER_SUCCESS_MATCH"
								},
								"values": [
									{
										"value": {
											"name": "opencv",
											"id": "94756ea97e399882b121da8bb2de55e2"
										}
									}
								]
							}
						]
					},
					"confirmationStatus": "NONE"
				},
				"operating_system": {
					"name": "operating_system",
					"value": "ubuntu",
					"resolutions": {
						"resolutionsPerAuthority": [
							{
								"authority": "amzn1.erauthority.echosdk.amzn1.ask.skill.79c68afc19b14e1aa7286481798feabf.operating_system",
								"status": {
									"code": "ER_SUCCESS_MATCH"
								},
								"values": [
									{
										"value": {
											"name": "ubuntu",
											"id": "10"
										}
									}
								]
							}
						]
					},
					"confirmationStatus": "NONE"
				},
				"software_management_library": {
					"name": "software_management_library",
					"confirmationStatus": "NONE"
				}
			}
		}
	}
},
	{
	"version": "1.0",
	"session": {
		"new": False,
		"attributes": {
			"complete_code_now_id": 0,
			"question_now_id": 1,
			"questions_urls": [
				"https://superuser.com/questions/678568/installopencvincentos",
				"https://superuser.com/questions/391021/homebrewiscowardlyrefusingtoinstallopencv/395060",
				"https://stackoverflow.com/questions/50416424/modulenotfounderrornomodulenamedopencv",
				"https://stackoverflow.com/questions/47512464/permissionerrorininstallingopencvcontribpython"
			],
			"requested_value": "give_answer",
			"complete_answer": [],
			"complete_code": [],
			"previous_intent_attributes": "",
			"previous_intent": "",
			"comments_ids": [],
			"answers_ids": [
				725799,
				682933,
				1090961
			],
			"previous_requested_value": "next_question",
			"question_name": "Install OpenCV in CentOS",
			"answer_now_id": 0,
			"comment_now_id": 0
		},
	},
	"request": {
		"type": "IntentRequest",
		"requestId": "amzn1.echoapi.request.7308090ce8ad47bcb07dbae917caff3e",
		"timestamp": "20181011T15:25:22Z",
		"locale": "enIN",
		"intent": {
			"name": "AnswerIntent",
			"confirmationStatus": "NONE",
			"slots": {
				"answer": {
					"name": "answer",
					"value": "no",
					"resolutions": {
						"resolutionsPerAuthority": [
							{
								"authority": "amzn1.erauthority.echosdk.amzn1.ask.skill.79c68afc19b14e1aa7286481798feabf.answer",
								"status": {
									"code": "ER_SUCCESS_MATCH"
								},
								"values": [
									{
										"value": {
											"name": "no",
											"id": "0"
										}
									}
								]
							}
						]
					},
					"confirmationStatus": "NONE"
				}
			}
		}
	}
},
	{
	"version": "1.0",
	"session": {
		"new": False,
		"attributes": {
			"complete_code_now_id": 0,
			"question_now_id": 2,
			"questions_urls": [
				"https://superuser.com/questions/678568/installopencvincentos",
				"https://superuser.com/questions/391021/homebrewiscowardlyrefusingtoinstallopencv/395060",
				"https://stackoverflow.com/questions/50416424/modulenotfounderrornomodulenamedopencv",
				"https://stackoverflow.com/questions/47512464/permissionerrorininstallingopencvcontribpython"
			],
			"requested_value": "give_answer",
			"complete_answer": [],
			"complete_code": [],
			"previous_intent_attributes": "",
			"previous_intent": "",
			"comments_ids": [],
			"answers_ids": [
				391030,
				395060,
				407467
			],
			"previous_requested_value": "next_question",
			"question_name": "Homebrew is &quot;cowardly refusing&quot; to install OpenCV",
			"answer_now_id": 0,
			"comment_now_id": 0
		},
	},
	"request": {
		"type": "IntentRequest",
		"requestId": "amzn1.echoapi.request.4b917055c80545fb8a0d36d9cc39f583",
		"timestamp": "20181011T15:26:32Z",
		"locale": "enIN",
		"intent": {
			"name": "AnswerIntent",
			"confirmationStatus": "NONE",
			"slots": {
				"answer": {
					"name": "answer",
					"value": "yes",
					"resolutions": {
						"resolutionsPerAuthority": [
							{
								"authority": "amzn1.erauthority.echosdk.amzn1.ask.skill.79c68afc19b14e1aa7286481798feabf.answer",
								"status": {
									"code": "ER_SUCCESS_MATCH"
								},
								"values": [
									{
										"value": {
											"name": "yes",
											"id": "1"
										}
									}
								]
							}
						]
					},
					"confirmationStatus": "NONE"
				}
			}
		}
	}
},
	{
	"version": "1.0",
	"session": {
		"new": False,
		"attributes": {
			"complete_code_now_id": 0,
			"question_now_id": 2,
			"questions_urls": [
				"https://superuser.com/questions/678568/installopencvincentos",
				"https://superuser.com/questions/391021/homebrewiscowardlyrefusingtoinstallopencv/395060",
				"https://stackoverflow.com/questions/50416424/modulenotfounderrornomodulenamedopencv",
				"https://stackoverflow.com/questions/47512464/permissionerrorininstallingopencvcontribpython"
			],
			"requested_value": "give_comment",
			"complete_answer": {
				"comment": "Owner of the question said If I do that I get: Cannot write to /usr/local/Cellar. A person said Did you ever mess around with chmod, possibly in combination with sudo there? Try sudo chown R USER /usr/local. Does it work after that? If not, please post a complete ls la listing of /usr/local and what brew doctor says. Owner of the question said Warning: It appears you have MacPorts or Fink installed. Software installed with other package managers causes known problems for Homebrew. If a formula fails to build, uninstall MacPorts/Fink and try again. Error: Unsatisfied external dependency: numpy Homebrew does not provide Python dependencies, easy_install does: easy_install numpy. A person said Ahah, see, we're getting there. For the future, please include things like these in your question, we can't magically guess anything. I don't understand your latest question please edit your original post and include the ls la of /usr/local. Also, maybe think about uninstalling MacPorts or Fink, whatever you have. A person said That's probably not enough info. The group should probably be staff. But this is the third time I've asked: Please post the complete output of ls la /usr/local in your original question. I'm glad to help, but you need to help a bit as well!.",
				"answer_text": "\nYou do not need sudo for Homebrew\nAs OpenCV now exists in homebrew/science, run the following:\nbrew tap homebrew/science\nbrew install opencv\n\nHomebrew never needs elevated privileges for anything except for when there are some conflicts with other installed libraries:\n\nHomebrew is designed to work without using sudo. You can decide to use it but we strongly recommend not to do so. If you have used sudo and run into a bug then it is likely to be the cause.\n\nIf you can't install it without sudo, make sure you own /usr/local and have the correct permissions also by running this script. Running brew doctor will also generally give you some good hints.\n For code and answer please refer to the response card in your alexa app. Do you want to hear the comments to this answer.",
				"card": "\nYou do not need sudo for Homebrew\nAs OpenCV now exists in homebrew/science, run the following:\nbrew tap homebrew/science\nbrew install opencv\n\nHomebrew never needs elevated privileges for anything except for when there are some conflicts with other installed libraries:\n\nHomebrew is designed to work without using sudo. You can decide to use it but we strongly recommend not to do so. If you have used sudo and run into a bug then it is likely to be the cause.\n\nIf you can't install it without sudo, make sure you own /usr/local and have the correct permissions also by running this script. Running brew doctor will also generally give you some good hints.\n\nCode : \nbrew tap homebrew/science\nbrew install opencv\n"
			},
			"complete_code": [],
			"previous_intent_attributes": "",
			"previous_intent": "",
			"comments_ids": [],
			"answers_ids": [
				391030,
				395060,
				407467
			],
			"previous_requested_value": "give_answer",
			"question_name": "Homebrew is &quot;cowardly refusing&quot; to install OpenCV",
			"answer_now_id": 1,
			"comment_now_id": 0
		},
	},
	"request": {
		"type": "IntentRequest",
		"requestId": "amzn1.echoapi.request.7aa9bbad17224f07ad3d39977f979dd5",
		"timestamp": "20181011T15:27:24Z",
		"locale": "enIN",
		"intent": {
			"name": "AnswerIntent",
			"confirmationStatus": "NONE",
			"slots": {
				"answer": {
					"name": "answer",
					"value": "repeat",
					"resolutions": {
						"resolutionsPerAuthority": [
							{
								"authority": "amzn1.erauthority.echosdk.amzn1.ask.skill.79c68afc19b14e1aa7286481798feabf.answer",
								"status": {
									"code": "ER_SUCCESS_MATCH"
								},
								"values": [
									{
										"value": {
											"name": "repeat",
											"id": "2"
										}
									}
								]
							}
						]
					},
					"confirmationStatus": "NONE"
				}
			}
		}
	}
},
	{
	"version": "1.0",
	"session": {
		"new": False,
		"attributes": {
			"complete_code_now_id": 0,
			"question_now_id": 2,
			"questions_urls": [
				"https://superuser.com/questions/678568/installopencvincentos",
				"https://superuser.com/questions/391021/homebrewiscowardlyrefusingtoinstallopencv/395060",
				"https://stackoverflow.com/questions/50416424/modulenotfounderrornomodulenamedopencv",
				"https://stackoverflow.com/questions/47512464/permissionerrorininstallingopencvcontribpython"
			],
			"requested_value": "give_comment",
			"complete_answer": {
				"comment": "Owner of the question said If I do that I get: Cannot write to /usr/local/Cellar. A person said Did you ever mess around with chmod, possibly in combination with sudo there? Try sudo chown R USER /usr/local. Does it work after that? If not, please post a complete ls la listing of /usr/local and what brew doctor says. Owner of the question said Warning: It appears you have MacPorts or Fink installed. Software installed with other package managers causes known problems for Homebrew. If a formula fails to build, uninstall MacPorts/Fink and try again. Error: Unsatisfied external dependency: numpy Homebrew does not provide Python dependencies, easy_install does: easy_install numpy. A person said Ahah, see, we're getting there. For the future, please include things like these in your question, we can't magically guess anything. I don't understand your latest question please edit your original post and include the ls la of /usr/local. Also, maybe think about uninstalling MacPorts or Fink, whatever you have. A person said That's probably not enough info. The group should probably be staff. But this is the third time I've asked: Please post the complete output of ls la /usr/local in your original question. I'm glad to help, but you need to help a bit as well!.",
				"answer_text": "\nYou do not need sudo for Homebrew\nAs OpenCV now exists in homebrew/science, run the following:\nbrew tap homebrew/science\nbrew install opencv\n\nHomebrew never needs elevated privileges for anything except for when there are some conflicts with other installed libraries:\n\nHomebrew is designed to work without using sudo. You can decide to use it but we strongly recommend not to do so. If you have used sudo and run into a bug then it is likely to be the cause.\n\nIf you can't install it without sudo, make sure you own /usr/local and have the correct permissions also by running this script. Running brew doctor will also generally give you some good hints.\n For code and answer please refer to the response card in your alexa app. Do you want to hear the comments to this answer.",
				"card": "\nYou do not need sudo for Homebrew\nAs OpenCV now exists in homebrew/science, run the following:\nbrew tap homebrew/science\nbrew install opencv\n\nHomebrew never needs elevated privileges for anything except for when there are some conflicts with other installed libraries:\n\nHomebrew is designed to work without using sudo. You can decide to use it but we strongly recommend not to do so. If you have used sudo and run into a bug then it is likely to be the cause.\n\nIf you can't install it without sudo, make sure you own /usr/local and have the correct permissions also by running this script. Running brew doctor will also generally give you some good hints.\n\nCode : \nbrew tap homebrew/science\nbrew install opencv\n"
			},
			"complete_code": [],
			"previous_intent_attributes": "",
			"previous_intent": "",
			"comments_ids": [],
			"answers_ids": [
				391030,
				395060,
				407467
			],
			"previous_requested_value": "give_answer",
			"question_name": "Homebrew is &quot;cowardly refusing&quot; to install OpenCV",
			"answer_now_id": 1,
			"comment_now_id": 0
		},
	},
	"request": {
		"type": "IntentRequest",
		"requestId": "amzn1.echoapi.request.33ea681d25ab41f89f55a2321e5802b2",
		"timestamp": "20181011T15:29:22Z",
		"locale": "enIN",
		"intent": {
			"name": "AnswerIntent",
			"confirmationStatus": "NONE",
			"slots": {
				"answer": {
					"name": "answer",
					"value": "yes",
					"resolutions": {
						"resolutionsPerAuthority": [
							{
								"authority": "amzn1.erauthority.echosdk.amzn1.ask.skill.79c68afc19b14e1aa7286481798feabf.answer",
								"status": {
									"code": "ER_SUCCESS_MATCH"
								},
								"values": [
									{
										"value": {
											"name": "yes",
											"id": "1"
										}
									}
								]
							}
						]
					},
					"confirmationStatus": "NONE"
				}
			}
		}
	}
},
	{
	"version": "1.0",
	"session": {
		"new": False,
		"attributes": {
			"complete_code_now_id": 0,
			"question_now_id": 2,
			"questions_urls": [
				"https://superuser.com/questions/678568/installopencvincentos",
				"https://superuser.com/questions/391021/homebrewiscowardlyrefusingtoinstallopencv/395060",
				"https://stackoverflow.com/questions/50416424/modulenotfounderrornomodulenamedopencv",
				"https://stackoverflow.com/questions/47512464/permissionerrorininstallingopencvcontribpython"
			],
			"requested_value": "give_answer",
			"complete_answer": {
				"comment": "Owner of the question said If I do that I get: Cannot write to /usr/local/Cellar. A person said Did you ever mess around with chmod, possibly in combination with sudo there? Try sudo chown R USER /usr/local. Does it work after that? If not, please post a complete ls la listing of /usr/local and what brew doctor says. Owner of the question said Warning: It appears you have MacPorts or Fink installed. Software installed with other package managers causes known problems for Homebrew. If a formula fails to build, uninstall MacPorts/Fink and try again. Error: Unsatisfied external dependency: numpy Homebrew does not provide Python dependencies, easy_install does: easy_install numpy. A person said Ahah, see, we're getting there. For the future, please include things like these in your question, we can't magically guess anything. I don't understand your latest question please edit your original post and include the ls la of /usr/local. Also, maybe think about uninstalling MacPorts or Fink, whatever you have. A person said That's probably not enough info. The group should probably be staff. But this is the third time I've asked: Please post the complete output of ls la /usr/local in your original question. I'm glad to help, but you need to help a bit as well!.",
				"answer_text": "\nYou do not need sudo for Homebrew\nAs OpenCV now exists in homebrew/science, run the following:\nbrew tap homebrew/science\nbrew install opencv\n\nHomebrew never needs elevated privileges for anything except for when there are some conflicts with other installed libraries:\n\nHomebrew is designed to work without using sudo. You can decide to use it but we strongly recommend not to do so. If you have used sudo and run into a bug then it is likely to be the cause.\n\nIf you can't install it without sudo, make sure you own /usr/local and have the correct permissions also by running this script. Running brew doctor will also generally give you some good hints.\n For code and answer please refer to the response card in your alexa app. Do you want to hear the comments to this answer.",
				"card": "\nYou do not need sudo for Homebrew\nAs OpenCV now exists in homebrew/science, run the following:\nbrew tap homebrew/science\nbrew install opencv\n\nHomebrew never needs elevated privileges for anything except for when there are some conflicts with other installed libraries:\n\nHomebrew is designed to work without using sudo. You can decide to use it but we strongly recommend not to do so. If you have used sudo and run into a bug then it is likely to be the cause.\n\nIf you can't install it without sudo, make sure you own /usr/local and have the correct permissions also by running this script. Running brew doctor will also generally give you some good hints.\n\nCode : \nbrew tap homebrew/science\nbrew install opencv\n"
			},
			"complete_code": [],
			"previous_intent_attributes": "",
			"previous_intent": "",
			"comments_ids": [],
			"answers_ids": [
				391030,
				395060,
				407467
			],
			"previous_requested_value": "give_comment",
			"question_name": "Homebrew is &quot;cowardly refusing&quot; to install OpenCV",
			"answer_now_id": 1,
			"comment_now_id": 0
		},
	},
	"request": {
		"type": "IntentRequest",
		"requestId": "amzn1.echoapi.request.df410ee794c34a1da037fab4a34e543d",
		"timestamp": "20181011T15:30:21Z",
		"locale": "enIN",
		"intent": {
			"name": "AnswerIntent",
			"confirmationStatus": "NONE",
			"slots": {
				"answer": {
					"name": "answer",
					"value": "yes",
					"resolutions": {
						"resolutionsPerAuthority": [
							{
								"authority": "amzn1.erauthority.echosdk.amzn1.ask.skill.79c68afc19b14e1aa7286481798feabf.answer",
								"status": {
									"code": "ER_SUCCESS_MATCH"
								},
								"values": [
									{
										"value": {
											"name": "yes",
											"id": "1"
										}
									}
								]
							}
						]
					},
					"confirmationStatus": "NONE"
				}
			}
		}
	}
},
	{
	"version": "1.0",
	"session": {
		"new": True,
	},
	"request": {
		"type": "IntentRequest",
		"requestId": "amzn1.echoapi.request.651b8e2237e34700b3d670971c33c05a",
		"timestamp": "20181011T15:32:19Z",
		"locale": "enIN",
		"intent": {
			"name": "Error_Intent",
			"confirmationStatus": "NONE",
			"slots": {
				"error_name": {
					"name": "error_name",
					"value": "indentation error in python",
					"confirmationStatus": "NONE"
				}
			}
		}
	}
},
	{
	"version": "1.0",
	"session": {
		"new": True,
	},
	"request": {
		"type": "IntentRequest",
		"requestId": "amzn1.echoapi.request.058e5a73c23141a69e640d4546126e1e",
		"timestamp": "20181011T15:33:46Z",
		"locale": "enIN",
		"intent": {
			"name": "Comparision_Intent",
			"confirmationStatus": "NONE",
			"slots": {
				"Comparision_a": {
					"name": "Comparision_a",
					"value": "python",
					"resolutions": {
						"resolutionsPerAuthority": [
							{
								"authority": "amzn1.erauthority.echosdk.amzn1.ask.skill.79c68afc19b14e1aa7286481798feabf.comaprision_a",
								"status": {
									"code": "ER_SUCCESS_MATCH"
								},
								"values": [
									{
										"value": {
											"name": "Python",
											"id": "a7f5f35426b927411fc9231b56382173"
										}
									}
								]
							}
						]
					},
					"confirmationStatus": "NONE"
				},
				"Comparision_b": {
					"name": "Comparision_b",
					"value": "c",
					"resolutions": {
						"resolutionsPerAuthority": [
							{
								"authority": "amzn1.erauthority.echosdk.amzn1.ask.skill.79c68afc19b14e1aa7286481798feabf.Comaparision_b",
								"status": {
									"code": "ER_SUCCESS_MATCH"
								},
								"values": [
									{
										"value": {
											"name": "C",
											"id": "0d61f8370cad1d412f80b84d143e1257"
										}
									},
									{
										"value": {
											"name": "C#",
											"id": "d7efa19fbe7d3972fd5adb6024223d74"
										}
									},
									{
										"value": {
											"name": "C++",
											"id": "f6f87c9fdcf8b3c3f07f93f1ee8712c9"
										}
									}
								]
							}
						]
					},
					"confirmationStatus": "NONE"
				}
			}
		}
	}
}]
	return temp_data