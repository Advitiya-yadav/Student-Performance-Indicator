# ScoreSense – Student Score Prediction System

🚀 **[Live Demo](https://student-performance-indicator-8uacd9elzjfolenx6j4nbs.streamlit.app/)**

ScoreSense is an end-to-end machine learning system that predicts a student's Math score based on demographic and academic input features.

---

## 📌 Problem Statement

Build a regression system that predicts the Math score of a student using:
- Gender
- Race / Ethnicity
- Parental level of education
- Lunch type
- Test preparation course
- Reading score
- Writing score

---

## 📊 Dataset

- ~1,000 student records
- Structured tabular dataset
- Mix of categorical and numerical features
- Supervised regression problem

---

## 🛠 Tech Stack

- Python
- Scikit-learn
- Pandas & NumPy
- Matplotlib
- Flask
- Streamlit
- Docker

---

## ⚙️ Model Development

Multiple regression models were evaluated:
- Linear Regression
- Ridge Regression
- Random Forest Regressor
- XGBoost Regressor
- CatBoost Regressor
- AdaBoost Regressor
- Decision Tree Regressor
- K-Nearest Neighbors

### 🏆 Best Model

Ridge Regression achieved the best performance:
- **R² Score: 0.88**
- Evaluated on held-out test dataset

---

## 🧠 Engineering Highlights

- Modular ML pipeline architecture
- Custom exception handling
- Logging system implementation
- Reproducible training workflow
- Model serialization and loading
- Separate training and prediction pipelines

---

## 🌐 Deployment

- Flask backend for prediction API (`application.py`)
- Streamlit-based interactive web interface (`streamlit_app.py`)
- Docker-ready project structure

---

## 📂 Project Structure

```
student-performance-indicator/
│
├── src/
│   ├── components/
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipeline/
│   │   ├── __init__.py
│   │   └── train_pipeline.py
│   ├── __init__.py
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── notebook/
│   ├── 1. EDA STUDENT PERFORMANCE.ipynb
│   └── 2. MODEL TRAINING.ipynb
│
├── templates/
│   ├── home.html
│   └── index.html
│
├── artifacts/
├── logs/
├── predict_pipeline.py
├── application.py
├── streamlit_app.py
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🚀 Future Improvements

- Cross-validation enhancement
- Model monitoring
- Cloud deployment scaling

---

## 👨‍💻 Author

Advitiya Yadav
B.Tech Computer Science – NIT Goa