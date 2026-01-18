import streamlit as st
import numpy as np
import pickle
import sklearn
st.title("Income Predictor")


st.set_page_config(page_title='Income Predictor')

# st.camera_input(label='camera')
# st.button(label='Click Here')
# if st.button("Ballons"):
#     st.ballons()
# st.write("I dont what to do ")
# st.error("This is errors")
# Insert a chat message container.
with open("model.pkl",'rb') as file:
    model=pickle.load(file) 

input=st.number_input(label="Enter Experience in years",min_value=0.0,max_value=10.0,value=0.5,step=0.1) 



if st.button("Predict"):
    predictions=model.predict([[input]])[0]
    st.success(predictions)  
    st.balloons()  

