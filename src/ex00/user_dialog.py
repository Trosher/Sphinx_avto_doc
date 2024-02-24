"""The module responsible for communication and interaction with the user"""
# ex00/user_dialog.py

from random import choice

def print_response_and_question(question, questions):
    """Print a survey result to a user
    
    Args:
        question (str): Question and answer positions from a json document
        questions (dict): json document
        
    Functionality:
        - Print a question and random answer from the list of available answers
    """
    print("______________________________________________")
    print("questions: ", questions[question]['questions'])
    print("answer: ", choice(questions[question]['response']), "\n")

def get_body_parameters():
    """Obtaining parameters of the hypothesized response when answering a question
    
    Returns:
        param (list): list of parameters
        
    Functionality:
        - Request parameters from user in positive integers foreach
        - If the parameters do not match the expected ones, it interrupts the input and starts it again notifying the user
    """
    try:
        respiration = int(input("Responder's heart beats per minute: "))
        heart_rate = int(input("Number of breaths per minute for the responder: "))
        blushing_level = int(input("Sheepdog's level of embarrassment: "))
        pupillary_dilation = int(input("The size of the responder's pupil: "))
        print("______________________________________________\n")
        if not (respiration > 0 and heart_rate > 0 and blushing_level > 0 and pupillary_dilation > 0):
            raise ValueError
        return respiration, heart_rate, blushing_level, pupillary_dilation
    except Exception:
        print("Invalid input\n\
parameters must be non-negative integers. try again.")
        return get_body_parameters()

def sum_param(param_body):
    """Summing up the parameters
    
    Args:
        param_body (dict): dictionary of parameters
        
    Functionality:
        - Adds the newly received parameters from the get_body_parameters function to the total sum of the parameters
    """
    param = get_body_parameters()
    param_body['respiration'] += param[0] 
    param_body['heart_rate'] += param[1] 
    param_body['blushing_level'] += param[2] 
    param_body['pupillary_dilation'] += param[3]
    
def check_responder(param_body, cunt_q):
    """Checking the interviewee for a replicant
    
    Args:
        param_body (dict): dictionary of parameters
        cunt_q (int): number of questions asked
        
    Functionality:
        - Check if the parameters match by dividing the sum of all parameters by the number of questions and comparing with the expected average
        - Prints the result of the interviewee
    """
    if 10 <= param_body['respiration'] / cunt_q <= 20 and 45 <= param_body['heart_rate'] / cunt_q <= 115 \
        and 3 <= param_body['blushing_level'] / cunt_q <= 5 and 1 <= param_body['pupillary_dilation'] / cunt_q <= 10:
        print("The person being interviewed is a human being")
    else:
        print("It's a replicant")