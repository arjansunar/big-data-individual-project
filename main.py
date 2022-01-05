import streamlit as st
import joblib

st.title("Spam classifier")

st.header("Find out the spam")

usr_input = st.text_area("Enter the message")

if st.button("Predict"):
    print("predict clicked")
    vectorizer = joblib.load(open("./model_&_vectorizer/text-vectorizer", 'rb'))
    model = joblib.load(open("./model_&_vectorizer/spam-classifier-model", 'rb'))

    vectorized_input = vectorizer.transform([usr_input])
    if model.predict(vectorized_input)[0] == 1:
        st.markdown("## ***SPAM***")
    else: 
        st.markdown("## ***HAM***")

