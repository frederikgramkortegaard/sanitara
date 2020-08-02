""" """

import re
import typing
from typing import Dict
from processing import machines
from processing.machines.models import *
from processing.heuristics.regex import *
from processing.heuristics.lookup_tables import *


def predict(message: str) -> Dict:
    """ Combination of every required
        pipeline function,
        returns a final prediction
    """

    def _predict(model, message: str, name: str) -> Dict:
        """ Dynamic inner-method for 
            calling different prediction
            services
        """

        out = {
            "name": name,
            "prediction": None,
            "err": None
        }

        # Lookup table implementation
        if index_of_lookup_tables[name] and index_of_lookup_tables[name][message]:
            out['prediction'] = 1
            return out
        elif model == False:
            out['prediction'] = 0
            return out

        if model == None:
            out['err'] = "Model is None"
            return out

        # Model prediction implementation
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
            _predict(False, message, "phishing"),
            _predict(False, message, "whitelist"),
            _predict(False, message, "blacklist")
        ]
    except Exception as e:
        out['err'] = str(e)

    return out