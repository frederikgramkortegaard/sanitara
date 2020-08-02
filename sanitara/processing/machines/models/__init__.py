""" """

import os
from joblib import load

# Load sklearn pornography detection
# model and returns it.  
# currently hardcoded relative-path.

model_name = sorted(list(filter(lambda x: "model_" and ".joblib" in x, os.listdir("./processing/machines/models"))))[-1]
print(f'Loading model: {model_name} from ./processing/machines/models')
pornography_detection_model = load(f"./processing/machines/models/{model_name}")