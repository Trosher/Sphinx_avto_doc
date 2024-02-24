"""The central main module of the program"""
# ex00/main.py

from pars_json import get_json
from user_dialog import print_response_and_question, sum_param, check_responder
from os.path import dirname

from functools import wraps
from time import perf_counter
from loguru import logger

def Loger(func):
    """Dicorator function to collect basic logs about the function
    
    Args:
        func (function): The function that will be decorated
        
    Returns:
        function result: Returns the result of the function execution if there is no result or an error, returns None
        
    Functionality:
        - Reports the start time of the function being dicored
        - Reports the completion time of the dicorized function
        - Reports the total execution time of the function
        - In case of errors, intercepts them and outputs them to stdout by default
        - When an error occurs, it does not allow to urgently terminate the program
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = None
        logger.info(f"function start: ({func.__name__}) with parameters: {args} :\n")
        start = perf_counter()
        try:
            result = func(*args, **kwargs)
            logger.info(f"The function ({func.__name__}) ended with the result: {result}")
            logger.info(f"The function ({func.__name__}) has been completed for {(perf_counter() - start):.4f}\n")
        except Exception as e:
                logger.exception(f"The function ({func.__name__}) ended with an error", e)
        return result
    return wrapper

@Loger 
def main():
    """Start function for the operation of the survey program"""
    questions = get_json(dirname(__file__)+"\\questions.json")
    if questions:
        param_body = {'respiration':0,'heart_rate':0,'blushing_level':0,'pupillary_dilation':0}
        for question in questions:
            print_response_and_question(question, questions)
            sum_param(param_body)
        check_responder(param_body, len(questions))

if __name__ == "__main__":
    main()