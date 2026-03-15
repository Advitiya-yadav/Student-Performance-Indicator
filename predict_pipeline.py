import os
import sys
import pandas as pd
import numpy as np
import joblib
from pathlib import Path

def load_object(file_path):
    return joblib.load(file_path)

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        root = Path(__file__).parent
        model_path = root / "artifacts" / "model.pkl"
        preprocessor_path = root / "artifacts" / "preprocessor.pkl"
        model = load_object(model_path)
        preprocessor = load_object(preprocessor_path)
        scaled_data = preprocessor.transform(features)
        prediction = model.predict(scaled_data)
        return prediction

class CustomData:
    def __init__(self, gender, race_ethnicity, parental_level_of_education, lunch, test_preparation_course, reading_score, writing_score):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        return pd.DataFrame({
            'gender': [self.gender],
            'race_ethnicity': [self.race_ethnicity],
            'parental_level_of_education': [self.parental_level_of_education],
            'lunch': [self.lunch],
            'test_preparation_course': [self.test_preparation_course],
            'reading_score': [self.reading_score],
            'writing_score': [self.writing_score]
        })