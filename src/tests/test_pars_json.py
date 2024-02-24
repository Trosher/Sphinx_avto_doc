"""Testing module for reading json files"""
# tests/test_pars_json.py

from ..ex00 import pars_json as pj

def setup_module(module):
    """Output the message about the start of the test module"""
    print (f"Start module {module}")

def setup_function(function):
    """Display a message about the start of the test function"""
    print (f"\n\nStart test: {function}")

def teardown_function(function):
    """Display a message indicating that the test function has been completed"""
    print(f"\nEnd test: {function}")
    
def test_pars_json():
    """Function for testing the reading of json file"""
    assert pj.get_json("questions.json")
    
def test_err_pars_json():
    """Testing the function of reading a json file with insufficient data"""
    assert not pj.get_json("questions_err.json")
    
def test_err0_pars_json():
    """Testing the function of reading a json file with no data"""
    assert not pj.get_json("questions_err0.json")