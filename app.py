import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download stopwords
nltk.download('stopwords')

# Initialize stemmer
ps = PorterStemmer()

# Function to clean and preprocess text
def transform_text(text):
    text = text.lower()
    text = text.split()

    # Remove non-alphanumeric
    y = [i for i in text if i.isalnum()]

    # Remove stopwords and punctuation
    y = [i for i in y if i not in stopwords.words('english') and i not in string.punctuation]

    # Stemming
    y = [ps.stem(i) for i in y]

    return " ".join(y)

# Load vectorizer and model
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# App title with icon
st.title("📧 Email/SMS Spam Classifier")

# Text input
input_sms = st.text_area("Enter the message")

# Predict button
if st.button('Predict'):
    # Preprocess
    transformed_sms = transform_text(input_sms)

    # Vectorize
    vector_input = tfidf.transform([transformed_sms])

    # Predict
    result = model.predict(vector_input)[0]

    # Display
    if result == 1:
        st.header("🚫 Spam")
    else:
        st.header("✅ Not Spam")
