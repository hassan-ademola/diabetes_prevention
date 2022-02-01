import streamlit as st
import pandas as pd
import pickle

st.title('Diabnotics')
st.write('Which of these do you feel today?')

age=st.slider('How old are you?',0,100,16)
gender=st.selectbox('Gender', ['Female','Male'])
st.select_slider('Hey',[1,2,3])
st.subheader('Which of these symptoms are you experiencing?')
columns = st.columns(2)
with columns[0]:
    polyuria=st.selectbox('Polyuria',['No','Yes'])
with columns[1]:
    polydipsia=st.selectbox('Polydipsia', ['No','Yes'])

columns = st.columns(2)
with columns[0]:
    sudden_weight_loss=st.selectbox('Sudden Weight Loss',['No','Yes'])
with columns[1]:
    weakness=st.selectbox('Weakness', ['No','Yes'])
          
columns = st.columns(2)
with columns[0]:
    polyphagia=st.selectbox('Polyphagia',['No','Yes'])
with columns[1]:
    genital_thrush=st.selectbox('Genital Thrush', ['No','Yes'])       

columns = st.columns(2)
with columns[0]:
    visual_blurring=st.selectbox('Blurry Vision',['No','Yes'])
with columns[1]:
    itching=st.selectbox('Itching', ['No','Yes'])       

columns = st.columns(2)
with columns[0]:
    irritability=st.selectbox('Irritability',['No','Yes'])
with columns[1]:
    delayed_healing=st.selectbox('Delayed Healing', ['No','Yes'])          

columns = st.columns(2)
with columns[0]:
    partial_paresis=st.selectbox('Partial Paresis',['No','Yes'])
with columns[1]:
    muscle_stiffness=st.selectbox('Muscle Stiffness', ['No','Yes'])     

columns = st.columns(2)
with columns[0]:
    alopecia=st.selectbox('Alopecia',['No','Yes'])
with columns[1]:
    obesity=st.selectbox('Obesity', ['No','Yes'])

features = pd.DataFrame([[age,gender,polyuria,polydipsia,sudden_weight_loss,weakness,polyphagia,genital_thrush,visual_blurring,itching,irritability,delayed_healing,partial_paresis,muscle_stiffness,alopecia,obesity]])
features.replace(['Yes','Positive','Male','No','Negative','Female'],[1,1,1,0,0,0],inplace=True)
model = pickle.load(open('model.pkl','rb'))
prediction = model.predict_proba(features)[:,1][0]
f'You are {round(prediction*100)}% likely to have diabetes'