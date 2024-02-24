"""The module responsible for reading json files with questions"""
# ex00/pars_json.py

print(__name__)
from loguru import logger
from json import load

def get_json(path:str):
    """ Function for reading json file
    
    Args:
        path (str): path to the json file
        
    Returns:
        data (str): json string
        
    Functionality:
        - Reads the json file
        - Checks the validity of the json file
        - If an error occurs or if the json is not valid, returns None and outputs an error message to stdout
    """
    try:
        with open(path,"rb") as json_file:
            if json_file:
                data = load(json_file)
            if len(data) < 10:
                raise ValueError
            return data
    except Exception as e:
        logger.exception(e)
        logger.error('''Check the validity of the json file and try again
                     the number of questions must be more than 9
                     questions themselves should be written in the format
                     {
                        "questions0": {
                            "questions": "Are you human?",
                            "response": [ "yes", "no", "possibly", "i don`t now" ]
                        },
                        ...
                     }''')