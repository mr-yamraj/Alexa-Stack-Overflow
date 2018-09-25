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
									"authority": "amzn1.er-authority.echo-sdk.amzn1.ask.skill.79c68afc-19b1-4e1a-a728-6481798feabf.library_name",
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
									"authority": "amzn1.er-authority.echo-sdk.amzn1.ask.skill.79c68afc-19b1-4e1a-a728-6481798feabf.operating_system",
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
				"questions_ids": [
					"14911365",
					"26592577"
				],
				"complete_code_now_id": 0,
				"question_now_id": 1,
				"requested_value": "give_answer",
				"complete_answer": [],
				"complete_code": [],
				"previous_intent_attributes": "",
				"previous_intent": "",
				"comments_ids": [],
				"answers_ids": [
					14916415,
					20216884,
					46598045,
					40884133
				],
				"previous_requested_value": "next_question",
				"question_name": "How to install OpenCV in ubuntu 12.04",
				"answer_now_id": 0,
				"comment_now_id": 0
			}
		},
		"request": {
			"type": "IntentRequest",
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
									"authority": "amzn1.er-authority.echo-sdk.amzn1.ask.skill.79c68afc-19b1-4e1a-a728-6481798feabf.answer",
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
				"questions_ids": [
					"14911365",
					"26592577"
				],
				"complete_code_now_id": 0,
				"question_now_id": 2,
				"requested_value": "give_answer",
				"complete_answer": [],
				"complete_code": [],
				"previous_intent_attributes": "",
				"previous_intent": "",
				"comments_ids": [],
				"answers_ids": [
					26595275,
					27020828,
					28347684
				],
				"previous_requested_value": "next_question",
				"question_name": "Installing OpenCV in Ubuntu 14.10",
				"answer_now_id": 0,
				"comment_now_id": 0
			}
		},
		"request": {
			"type": "IntentRequest",
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
									"authority": "amzn1.er-authority.echo-sdk.amzn1.ask.skill.79c68afc-19b1-4e1a-a728-6481798feabf.answer",
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
				"questions_ids": [
					"14911365",
					"26592577"
				],
				"complete_code_now_id": 0,
				"question_now_id": 2,
				"requested_value": "give_comment",
				"complete_answer": {
					"comment": " Owner of the question said Thank you. It was much easier than I thought.. A person said well, that's not a solution. Especially if someone requires Qt, CUDA, OpenNI.. Owner of the question said I'm using Qt, and everything is working.. A person said yes but you didn't build OpenCV with Qt support..",
					"answer_text": "\nUnless you have special reasons I would suggest installing the OpenCV that are already in the Ubuntu repository: sudo apt-get install libopencv-dev\nFor video codecs I suggest simply trying to install all ffmpeg and gstreamer related codec packages.\n For code and answer please refer to the response card in your alexa app. Do you want to hear the comments to this answer.",
					"card": "\nUnless you have special reasons I would suggest installing the OpenCV that are already in the Ubuntu repository: sudo apt-get install libopencv-dev\nFor video codecs I suggest simply trying to install all ffmpeg and gstreamer related codec packages.\n"
				},
				"complete_code": [],
				"previous_intent_attributes": "",
				"previous_intent": "",
				"comments_ids": [],
				"answers_ids": [
					26595275,
					27020828,
					28347684
				],
				"previous_requested_value": "give_answer",
				"question_name": "Installing OpenCV in Ubuntu 14.10",
				"answer_now_id": 1,
				"comment_now_id": 0
			}
		},
		"request": {
			"type": "IntentRequest",
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
									"authority": "amzn1.er-authority.echo-sdk.amzn1.ask.skill.79c68afc-19b1-4e1a-a728-6481798feabf.answer",
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
				"questions_ids": [
					"14911365",
					"26592577"
				],
				"complete_code_now_id": 0,
				"question_now_id": 2,
				"requested_value": "give_comment",
				"complete_answer": {
					"comment": " Owner of the question said Thank you. It was much easier than I thought.. A person said well, that's not a solution. Especially if someone requires Qt, CUDA, OpenNI.. Owner of the question said I'm using Qt, and everything is working.. A person said yes but you didn't build OpenCV with Qt support..",
					"answer_text": "\nUnless you have special reasons I would suggest installing the OpenCV that are already in the Ubuntu repository: sudo apt-get install libopencv-dev\nFor video codecs I suggest simply trying to install all ffmpeg and gstreamer related codec packages.\n For code and answer please refer to the response card in your alexa app. Do you want to hear the comments to this answer.",
					"card": "\nUnless you have special reasons I would suggest installing the OpenCV that are already in the Ubuntu repository: sudo apt-get install libopencv-dev\nFor video codecs I suggest simply trying to install all ffmpeg and gstreamer related codec packages.\n"
				},
				"complete_code": [],
				"previous_intent_attributes": "",
				"previous_intent": "",
				"comments_ids": [],
				"answers_ids": [
					26595275,
					27020828,
					28347684
				],
				"previous_requested_value": "give_answer",
				"question_name": "Installing OpenCV in Ubuntu 14.10",
				"answer_now_id": 1,
				"comment_now_id": 0
			}
		},
		"request": {
			"type": "IntentRequest",
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
									"authority": "amzn1.er-authority.echo-sdk.amzn1.ask.skill.79c68afc-19b1-4e1a-a728-6481798feabf.answer",
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
				"questions_ids": [
					"14911365",
					"26592577"
				],
				"complete_code_now_id": 0,
				"question_now_id": 2,
				"requested_value": "give_answer",
				"complete_answer": {
					"comment": " Owner of the question said Thank you. It was much easier than I thought.. A person said well, that's not a solution. Especially if someone requires Qt, CUDA, OpenNI.. Owner of the question said I'm using Qt, and everything is working.. A person said yes but you didn't build OpenCV with Qt support..",
					"answer_text": "\nUnless you have special reasons I would suggest installing the OpenCV that are already in the Ubuntu repository: sudo apt-get install libopencv-dev\nFor video codecs I suggest simply trying to install all ffmpeg and gstreamer related codec packages.\n For code and answer please refer to the response card in your alexa app. Do you want to hear the comments to this answer.",
					"card": "\nUnless you have special reasons I would suggest installing the OpenCV that are already in the Ubuntu repository: sudo apt-get install libopencv-dev\nFor video codecs I suggest simply trying to install all ffmpeg and gstreamer related codec packages.\n"
				},
				"complete_code": [],
				"previous_intent_attributes": "",
				"previous_intent": "",
				"comments_ids": [],
				"answers_ids": [
					26595275,
					27020828,
					28347684
				],
				"previous_requested_value": "give_comment",
				"question_name": "Installing OpenCV in Ubuntu 14.10",
				"answer_now_id": 1,
				"comment_now_id": 0
			}
		},
		"request": {
			"type": "IntentRequest",
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
									"authority": "amzn1.er-authority.echo-sdk.amzn1.ask.skill.79c68afc-19b1-4e1a-a728-6481798feabf.answer",
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
			"new": True
					},
		"request": {
			"type": "IntentRequest",
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
			"new": True
					},
		"request": {
			"type": "IntentRequest",
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
									"authority": "amzn1.er-authority.echo-sdk.amzn1.ask.skill.79c68afc-19b1-4e1a-a728-6481798feabf.comaprision_a",
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
									"authority": "amzn1.er-authority.echo-sdk.amzn1.ask.skill.79c68afc-19b1-4e1a-a728-6481798feabf.Comaparision_b",
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