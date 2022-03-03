import streamlit as st
import pandas as pd
import pickle
import time

st.title('Diabnotics')
st.subheader("This diagnostic tool predicts a patient's risk of diabetes")

columns = st.columns(2)
with columns[0]:
    age=st.slider('How old are you?',0,90,16)
with columns[1]:
    gender=st.selectbox('Gender', ['Female','Male'])

st.subheader('Which of these symptoms do you have?')
columns = st.columns(4)
with columns[0]:
    polyuria=st.selectbox('Excessive Peeing',['No','Yes'])
with columns[1]:
    polydipsia=st.selectbox('Extreme Thirst', ['No','Yes'])
with columns[2]:
    sudden_weight_loss=st.selectbox('Sudden Weight Loss',['No','Yes'])
with columns[3]:
    weakness=st.selectbox('Weakness', ['No','Yes'])
          
columns = st.columns(4)
with columns[0]:
    polyphagia=st.selectbox('Increased Appetite',['No','Yes'])
with columns[1]:
    genital_thrush=st.selectbox('Yeast Infection', ['No','Yes'])       
with columns[2]:
    visual_blurring=st.selectbox('Blurry Vision',['No','Yes'])
with columns[3]:
    itching=st.selectbox('Itching', ['No','Yes'])       

columns = st.columns(4)
with columns[0]:
    irritability=st.selectbox('Frustration',['No','Yes'])
with columns[1]:
    delayed_healing=st.selectbox('Delayed Healing', ['No','Yes'])          
with columns[2]:
    partial_paresis=st.selectbox('Muscle Weakness',['No','Yes'])
with columns[3]:
    muscle_stiffness=st.selectbox('Muscle Stiffness', ['No','Yes'])     
    
columns = st.columns(2)
with columns[0]:
    alopecia=st.selectbox('Hair Loss',['No','Yes'])
with columns[1]:
    obesity=st.selectbox('Obesity', ['No','Yes'])

features = pd.DataFrame([[age,gender,polyuria,polydipsia,sudden_weight_loss,weakness,polyphagia,genital_thrush,visual_blurring,itching,irritability,delayed_healing,partial_paresis,muscle_stiffness,alopecia,obesity]])

# encode categories
features.replace(['Yes','Positive','Male','No','Negative','Female'],[1,1,1,0,0,0],inplace=True)

# load trained model
model = pickle.load(open('model.pkl','rb'))

# predict probability of the case being diabetic
probability = model.predict_proba(features)[:,1][0]
percentage = round(probability*100)

my_bar = st.progress(0)
for percent_complete in range(percentage):
     time.sleep(0.02)
     my_bar.progress(percent_complete + 1)
if percentage<=50:
    st.success(f'You are **{percentage}%** likely to have diabetes')

elif 50<percentage<=75:
    st.warning(f'You are **{percentage}%** likely to have diabetes')

else:
    st.error(f'You are **{percentage}%** likely to have diabetes')
