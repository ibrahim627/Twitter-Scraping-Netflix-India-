#IMPORT MATERIAL
import streamlit as st
import pandas as pd
from PIL import Image
import snscrape.modules.twitter as sntwitter
from datetime import datetime
import numpy as np
import json
import base64

#BASICS
st.set_page_config(page_title="My Scraper.app")

#IMAGE UPLOAD
pic= Image.open(r"C:\Users\ELCOT\Desktop\twitter scraping\twitter scrape.png")
st.image(pic)

st.header("Twitter Scraping")

st.markdown("Twitter Scraping refers to the process of extracting data from Twitter. The extracted data can be used for a variety of purposes, such as sentiment analysis, market research, trend analysis, and more.")

st.subheader("Netflix India Tweets")



 
#IMPORT SCRAPPED DATE SET
df = pd.read_csv("Twitter Scraped Data.csv")

Submit = st.checkbox("Click To View Dataset")
if Submit:
    st.dataframe(df)

# DOWNLOAD OPTION
st.download_button("Download CSV File",df.to_csv(),
                   file_name='Twitter Scraped Data.csv',mime='csv')

#FILTER BY HASHTAG

st.header("Hashtag Filter Data") 

hashtag = st.text_input('Enter hashtag:')

def filter_data(hashtag, df):
    filtered_df = df[df['CONTENT'].str.contains(hashtag, na=False)]
    return filtered_df
      
if hashtag:
    filtered_df = filter_data(hashtag, df)
    st.write(filtered_df)
    
if st.button('Download CSV File'):
   
   csv = filtered_df.to_csv(index=False)
   b64 = base64.b64encode(csv.encode()).decode()
   href = f'<a href="data:file/csv;base64,{b64}" download="Hashtag dataset.csv">Download CSV File</a>'
   st.markdown(href, unsafe_allow_html=True)

if st.button("Download JSON File "):
    filtered_data_json = filtered_df.to_json(orient='records')
    b64 = base64.b64encode(filtered_data_json.encode()).decode() 
    href = f'<a href="data:application/json;base64,{b64}" download="Hashtag dataset.json">Download JSON File</a>'
    st.markdown(href, unsafe_allow_html=True)


#DATE RANGE FILTERING

st.header('Date Range Filter')

#CHANGE THE DATE FORMAT

df['DATE'] = pd.to_datetime(df['DATE'] )

Start_Date = st.date_input('Enter the Start date:',value= df["DATE"].min().date())
Start_Date = pd.to_datetime(Start_Date).strftime("%Y-%m-%d %H:%M:%S")


End_Date = st.date_input('Enter the End date:',value= df["DATE"].max().date())
End_Date = pd.to_datetime(End_Date).strftime("%Y-%m-%d %H:%M:%S")

#FILTERING DATE

filtered_date = df[(df["DATE"] >= Start_Date) & (df["DATE"] <= End_Date)]
st.write("Number of tweets:",filtered_date.shape[0])
st.dataframe(filtered_date)



#Add to download option as CSV

if st.button("Download file as csv"):
   
   csv = filtered_date.to_csv(index=False)
   b64 = base64.b64encode(csv.encode()).decode()
   href = f'<a href="data:file/csv;base64,{b64}" download="Date filter dataset.csv">Download CSV File</a>'
   st.markdown(href, unsafe_allow_html=True)

#Add to download option as JSON

if st.button("Download file as json"):
    filtered_data_json = filtered_date.to_json(orient='records')
    b64 = base64.b64encode(filtered_data_json.encode()).decode() 
    href = f'<a href="data:application/json;base64,{b64}" download="Date filter dataset.json">Download JSON File</a>'
    st.markdown(href, unsafe_allow_html=True)
    
