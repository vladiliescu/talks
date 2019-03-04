import json
import numpy as np
import os
import pickle
from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegression

from azureml.core.model import Model

def init():
    global model
    model_path = Model.get_model_path('iris')
    model =  pickle.load(open(model_path, "rb"))

def run(raw_data):
    data = json.loads(raw_data)
    values = data['Inputs']['input1']['Values']

    try:
        y = model.predict(values)
        output = np.column_stack([values, y]).tolist()
        return {
                "Results": {
                    "output1": {
                         "type": "hello",
                         "value": { 
                             "Values" : output
                            }
                        }
                    }
                }
    except Exception as e:
        return json.dumps({"error": str(e)})
