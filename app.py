import streamlit as st
import pickle
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

stopwords=stopwords.words('english')
stemer= PorterStemmer()

def text_process(x):
    y=nltk.word_tokenize(x.lower())
    k=[]
    for i in y:
        if i.isalnum():
            k.append(i)
    y=k[:]
    k.clear()
    for i in y:
        if i not in stopwords and i not in string.punctuation :
            k.append(i)
    y=k[:]
    k.clear()
    for i in y:
        k.append(stemer.stem(i))
    return ' '.join(k)

vactor=pickle.load(open('vectorizer.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))

st.title('SMS SPAM DETECTOR')
sms=st.text_input('enter the messege')
if st.button('predict'):
    transform_text = text_process(sms)
    convert_text=vactor.transform([transform_text])
    predicted_value = model.predict(convert_text)[0]

    if predicted_value==1:
        st.header('SPAM')
    else:
        st.header('ham')

