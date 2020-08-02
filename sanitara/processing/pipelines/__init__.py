""" """
import re
import typing
from typing import Dict

from processing.heuristics import regex
from processing import machines

model = machines.load_model()

def clean_message(message: str) -> str:
    """ Cleans input message 
        and makes it useable for prediction'
    """

    raise NotImplementedError()    


def predict(message: str) -> Dict:
    """ Combination of every required
        pipeline function,
        returns a final prediction
    """

    result = None
    out = {
        "prediction": None,
        "err": None,
        "input": message
    }

    try:
        #message = clean_message(message)
        out['prediction'] = machines.predict(model, message)
    except Exception as e:
        out['err'] = str(e)

    return out