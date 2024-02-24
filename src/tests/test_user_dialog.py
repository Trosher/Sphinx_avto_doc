"""User Communication Testing Module"""
# tests/test_user_dialog.py

from ..ex00 import user_dialog as us
from contextlib import redirect_stdout
import io

def setup_module(module):
    """Output the message about the start of the test module"""
    print (f"Start module {module}")

def setup_function(function):
    """Display a message about the start of the test function"""
    print (f"\n\nStart test: {function}")

def teardown_function(function):
    """Display a message indicating that the test function has been completed"""
    print(f"\nEnd test: {function}")

def test_get_body_parameters(monkeypatch):
    """Testing the function of capturing interviewer behavior data from the user"""
    responses = iter([1, 12, 13, 100])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    param_body = us.get_body_parameters()
    assert param_body[0] == 1
    assert param_body[1] == 12
    assert param_body[2] == 13
    assert param_body[3] == 100
        
def test_sum_param(monkeypatch):
    """Testing the fetching function of saving data on the behavior of the interviewee"""
    param_body = {'respiration':0,'heart_rate':0,
                  'blushing_level':0,'pupillary_dilation':0}
    responses = iter([1, 12, 13, 100])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    us.sum_param(param_body)
    assert param_body['respiration'] == 1
    assert param_body['heart_rate'] == 12
    assert param_body['blushing_level'] == 13
    assert param_body['pupillary_dilation'] == 100
        
def test_replicant_check_responder():
    """Testing the function to verify the interviewee's affiliation with replicants"""
    f = io.StringIO()
    param_body = {'respiration':0,'heart_rate':0,
                  'blushing_level':0,'pupillary_dilation':0}
    with redirect_stdout(f):
        us.check_responder(param_body, 1)
    assert f.getvalue() == "It's a replicant\n"
        
def test_no_replicant_check_responder():
    """Testing the function of verifying the interviewee's affinity to people"""
    f = io.StringIO()
    param_body = {'respiration':15,'heart_rate':50,
                  'blushing_level':4,'pupillary_dilation':2}
    with redirect_stdout(f):
        us.check_responder(param_body, 1)
    assert f.getvalue() == "The person being interviewed is a human being\n"
