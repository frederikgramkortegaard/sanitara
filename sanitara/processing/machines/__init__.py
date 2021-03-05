""" """

import os
import typing
from joblib import load



def predict(model, url: str) -> float:
    """ Directly interfaces the model
        and returns its prediction as either
        0.0 or 1.0
    """

    return float(model.predict([url])[0])
