import os
import sys
import numpy as np
import pandas as pd
import joblib
from sklearn.metrics import r2_score
from exception import CustomException

def save_object(file_path, obj):
    try:
        os.makedirs(os.path.dirname(str(file_path)), exist_ok=True)
        joblib.dump(obj, file_path)
    except Exception as e:
        raise CustomException(e, sys)

def load_object(file_path):
    try:
        return joblib.load(file_path)
    except Exception as e:
        raise CustomException(e, sys)