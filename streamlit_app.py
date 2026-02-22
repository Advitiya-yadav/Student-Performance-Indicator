import sys
import os

# Ensure project root is in Python path (for Streamlit Cloud)
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import streamlit as st
import pandas as pd
from src.pipeline.predict_pipeline import PredictPipeline, CustomData


st.set_page_config(page_title="Student Performance Predictor", layout="centered")

st.title("Student Performance Predictor 🧑‍🎓")
st.write("Enter student details to predict the Math score.")

st.divider()

# ---------------- INPUTS ---------------- #

gender = st.selectbox("Gender", ["male", "female"])

ethnicity = st.selectbox(
    "Race / Ethnicity",
    ["group A", "group B", "group C", "group D", "group E"]
)

parent_edu = st.selectbox(
    "Parental Level of Education",
    [
        "some high school",
        "high school",
        "some college",
        "associate's degree",
        "bachelor's degree",
        "master's degree"
    ]
)

lunch = st.selectbox("Lunch", ["standard", "free/reduced"])

test_prep = st.selectbox(
    "Test Preparation Course",
    ["none", "completed"]
)

reading = st.number_input("Reading Score", min_value=0, max_value=100, step=1)
writing = st.number_input("Writing Score", min_value=0, max_value=100, step=1)

st.divider()

# ---------------- PREDICTION ---------------- #

if st.button("Predict Math Score"):

    try:
        data = CustomData(
            gender=gender,
            race_ethnicity=ethnicity,
            parental_level_of_education=parent_edu,
            lunch=lunch,
            test_preparation_course=test_prep,
            reading_score=float(reading),
            writing_score=float(writing),
        )

        df = data.get_data_as_data_frame()

        pipeline = PredictPipeline()
        result = pipeline.predict(df)

        predicted_score = round(result[0], 2)

        st.success(f"🎯 Predicted Math Score: {predicted_score}")

    except Exception as e:
        st.error("Something went wrong during prediction.")
        st.exception(e)