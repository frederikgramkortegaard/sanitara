""" """
import re
import typing
from typing import Dict

from processing.heuristics import regex
from processing import machines
from processing.machines.models import *


def clean_message(message: str) -> str:
    """ Cleans input message 
        and makes it useable for prediction'
    """

    raise NotImplementedError()    

def _predict(model, message: str, name: str) -> Dict:
    out = {
        "name": name,
        "prediction": None,
        "err": None
    }

    if model == None:
        out['err'] = "Model is None"
    else: 
        try:
            out['prediction'] = machines.predict(model, message)
        except Exception as e:
            out['err'] = str(e)

    return out

def predict(message: str) -> Dict:
    """ Combination of every required
        pipeline function,
        returns a final prediction
    """

    out = {
        "predictions": None,
        "err": None,
        "input": message
    }
    print(_predict(pornography_detection_model, message, "porn"))

    try:
        out['predictions'] = [
            _predict(pornography_detection_model, message, "porn"),
            _predict(phishing_detection_model, message, "phishing")
        ]
    except Exception as e:
        out['err'] = str(e)

    print(out)

    return out