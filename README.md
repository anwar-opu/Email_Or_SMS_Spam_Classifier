# 📧 SMS/Email Spam Classifier

A simple Streamlit web app that classifies SMS or Email messages as **Spam** or **Not Spam** using NLP and a machine learning model.

🔗 Live App: [Click Here](https://sms-or-email-classifier.streamlit.app/)


## 🚀 How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```
---

## 📁 Files
```app.py``` – Main app

```model.pkl``` – Trained spam classifier model

```vectorizer.pkl``` – TF-IDF vectorizer

```requirements.txt``` – Dependencies

```sms_Spam_Classifier.ipynb``` - Model training

---

## 💡 Features

- Input any SMS or Email message
- Cleans and preprocesses text using:
  - Lowercasing
  - Tokenization
  - Stopword removal
  - Stemming
- Uses TF-IDF vectorization
- Predicts using a trained ML model

---

## 🛠 Tech Stack

- Python
- Streamlit
- Scikit-learn
- NLTK
- Pickle

---
