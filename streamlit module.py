import streamlit as st
import pandas as pd
from PIL import Image

header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()
model_training = st.beta_container()

with header:
    st.title('Lagos City Temperature')
    image = Image.open('temp.jpg')
    st.image(image)
    st.write("Know the temperature of your city Lagos over the past 100 years   ...")

with dataset:
    st.header('The temperature data')
    st.text('Lagos given its proximity to the ocean is generally a cooler city compared to most parts of Nigeria,' 
    'but it is also in a tropical region, hence, some days the temperature of the city appears to be unbearable with the scalding sun,' 
    'hence, I decided to investigate this by collecting data of the city temperature over the past 100 years to see if it has always been hot or'
    'there is an external factor at play here increasing the city temperature')
    data = pd.read_csv('tempdata.csv')
    st.write(data.head(20))
    st.subheader('Lagos city temperature data')
    st.line_chart(data['lagos_avg'])
    st.subheader('Global temperature data')
    st.line_chart(data['globe_avg'])

with features:
    st.header('The Features I created')
    st.markdown(' * **lagos_avg** - using the actual temperature gathered over the years, I used the exponential moving average to create this feature so as to easily see the changes in the temperature with time')
    st.markdown(' * **globe_avg** - using the actual temperature gathered over the years, I used the exponential moving average to create this feature so as to easily see the changes in the temperature with time')


with model_training:
    st.header('Time to train the model')
    st.text('As this is fully a data exploratory project, no models were trained.')
