import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
import nltk
nltk.download('stopwords')

ps = PorterStemmer()

def transform_text(text):
    # convert lower case
    text = text.lower()

    # Tokenization
    text = text.split()  # Tokenize by whitespace

    # Remove special characters -> #,%
    y = []
    for i in text:
      if i.isalnum():
        y.append(i)


    text = y[:]
    y.clear()

    for i in text:
      if i not in stopwords.words('english') and i not in string.punctuation:
        y.append(i)

    text = y[:]
    y.clear()

    for i in text:
      y.append(ps.stem(i))

    return " ".join(y)


tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("📧 Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):
  # 1. preprocess
  transform_sms =  transform_text(input_sms)
  # 2. vectorizer
  vector_input = tfidf.transform([transform_sms])
  # 3. predict
  result = model.predict(vector_input)
  # 4. Display
  if result == 1:
    st.header("Spam")
  else:
    st.header("Not Spam")
