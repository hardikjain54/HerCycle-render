import pickle
import pandas as pd
import streamlit as st
import datetime

def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSUalQw1trrCTAfTe9Lhz1rocCHrRxha3qSGA&usqp=CAU");
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
df = pd.read_csv(r"C:\Users\Hardik jain\OneDrive\Desktop\FedCycleData071012 (2).csv")
df.dropna(inplace=True)
df1 = df['EstimatedDayofOvulation']
df2 = df['LengthofLutealPhase']

st.header("Predict The Period Day")


d = st.date_input('When your last period start date',datetime.date(2023,4,18))
target = st.number_input('**LengthofCycle**', value=1)
FirstDayofHigh =  st.number_input('FirstDayofHigh ',value = 1)
EstimatedDayofOvulation = st.number_input(' Last Estimated Day of Ovulation', value=1)
Lastperiod = st.selectbox('About last periods',['Normal','Abnormal'])
#Weight = st.number_input('Weight',value = 25)
#Height = st.number_input('Height',value =26)

if st.button('Predict probability'):
    LengthofLutealPhase = target - EstimatedDayofOvulation
    if(LengthofLutealPhase>=14 | LengthofLutealPhase<=21):
         Result = 'Period is Normal'
    else:
         Result = 'Period is Ab Normal'
    TotalNumberofHighDays = EstimatedDayofOvulation - FirstDayofHigh
    TotalDaysofFertility = 4 + TotalNumberofHighDays
    #BMI = Weight/Height*Height



    input_df = pd.DataFrame(
        {'EstimatedDayofOvulation':[EstimatedDayofOvulation],'LengthofLutealPhase':[LengthofLutealPhase ],'TotalDaysofFertility': [TotalDaysofFertility], 'TotalNumberofHighDays': [TotalNumberofHighDays],'Result': [Result]})
    st.dataframe(input_df)

