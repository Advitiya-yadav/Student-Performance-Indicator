# ScoreSense – Student Score Prediction System

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

- Flask backend for prediction API
- Streamlit-based interactive web interface
- Docker-ready project structure

---

## 📂 Project Structure
student-performance-indicator/
│
├── src/
│ ├── components/
│ ├── pipeline/
│ │ ├── init.py
│ │ ├── predict_pipeline.py
│ │ └── train_pipeline.py
│ ├── init.py
│ ├── exception.py
│ ├── logger.py
│ └── utils.py
│
├── artifacts/
├── templates/
├── logs/
├── streamlit_app.py
├── application.py
├── requirements.txt
├── setup.py
├── Dockerfile
└── README.md

---

## 🚀 Future Improvements

- Hyperparameter tuning
- Cross-validation enhancement
- Model monitoring
- Cloud deployment scaling

---

## 👨‍💻 Author

Advitiya Yadav  
B.Tech Computer Science – NIT Goa