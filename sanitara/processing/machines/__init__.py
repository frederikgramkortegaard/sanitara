""" """

import os
import typing
from joblib import load

def load_model():
    """ Loads sklearn model and returns it,
        currently hardcoded relative-path.
    """

    model_name = sorted(list(filter(lambda x: "model_" and ".joblib" in x, os.listdir("./processing/machines/models"))))[-1]
    print(f'Loading model: {model_name} from "./processing/machines/models"')
    return load(f"./processing/machines/models/{model_name}")

def predict(model, url: str) -> float:
    """ Directly interfaces the model
        and returns its prediction as either
        0.0 or 1.1
    """

    return float(model.predict([url])[0])