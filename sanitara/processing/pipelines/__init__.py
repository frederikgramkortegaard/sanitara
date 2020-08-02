""" """
import re
import typing
from typing import Dict

from processing import machines
from processing.machines.models import *
from processing.heuristics.lookup_tables import *
from processing.heuristics.regex import *

def predict(message: str) -> Dict:
    """ Combination of every required
        pipeline function,
        returns a final prediction
    """

    def _predict(model, message: str, name: str) -> Dict:
        out = {
            "name": name,
            "prediction": None,
            "err": None
        }

        if index_of_lookup_tables[name] and index_of_lookup_tables[name][message]:
            out['prediction'] = 1
            return out

        if model == None:
            out['err'] = "Model is None"
            return out

        try:
            out['prediction'] = machines.predict(model, message)
        except Exception as e:
            out['err'] = str(e)

        return out

    out = {
        "predictions": None,
        "err": None,
        "input": message
    }

    try:
        out['predictions'] = [
            _predict(pornography_detection_model, message, "pornography"),
            _predict(phishing_detection_model, message, "phishing")
        ]
    except Exception as e:
        out['err'] = str(e)

    return out