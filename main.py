import pickle
import pandas as pd
import streamlit as st
import datetime

def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://media.istockphoto.com/id/1313684904/photo/beautiful-abstract-light-pink-feathers-on-white-background-white-feather-frame-on-pink.jpg?b=1&s=612x612&w=0&k=20&c=po_UbZB_lZpVVkOtFBmCYcr2uRpJWGxEqambC1swLTw=");
             background-attachment: fixed;
             background-size: contain


         }}
         </style>
         """,
        unsafe_allow_html=True
    )

add_bg_from_url()

LengthofCycle = ['10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                 '27', '28', '29', '30']

pipt = pickle.load(open("decision_tree.pkl", 'rb'))
df = pd.read_csv("FedCycleData071012 (2).csv")
df.dropna(inplace=True)
df1 = df['EstimatedDayofOvulation']
df2 = df['LengthofLutealPhase']

st.header("Predict The Period Day")


d = st.date_input('**When your last period start date**',datetime.date(2023,4,18))
target = st.number_input('**Length_of_Cycle**', value=1)
First_Day_of_High =  st.number_input('**First_Day_of_High**',value = 1)
Estimated_Day_of_Ovulation = st.number_input(' **Last_Estimated_Day_of_Ovulation**', value=1)
Last_Period = st.selectbox('**About last periods**',['Normal','Abnormal'])
#Weight = st.number_input('Weight',value = 25)
#Height = st.number_input('Height',value =26)

if st.button('Predict probability'):
    Length_of_Luteal_Phase = target - Estimated_Day_of_Ovulation
    if Length_of_Luteal_Phase>=14 and Length_of_Luteal_Phase <20 :
         Result = "Period is Normal"
    else:
        Result = "Period is Abnormal"
    Total_Number_of_HighDays = Estimated_Day_of_Ovulation - First_Day_of_High
    Total_Days_of_Fertility = 4 + Total_Number_of_HighDays
    #BMI = Weight/Height*Height




    input_df = pd.DataFrame(
        {'Estimated_Day_of_Ovulation':[Estimated_Day_of_Ovulation],'Length_of_Luteal_Phase':[Length_of_Luteal_Phase ],'Total_Days_of_Fertility': [Total_Days_of_Fertility], 'Total_Number_of_HighDays': [Total_Number_of_HighDays],'Result': [Result]})
    #st.dataframe(input_df)

    #st.markdown(input_df.style.hide().to_html(), unsafe_allow_html=True)
    styled_df = input_df.style.hide()

# Convert the styled DataFrame to HTML and display it using Streamlit's Markdown function
    st.markdown(styled_df.to_html(), unsafe_allow_html=True)






