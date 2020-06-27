# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 13:23:18 2020

@author: Ayush
"""


#news

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import streamlit as st
import re
import tweepy
from PIL import Image


def main():
    
    # Newspaper
    def paperHeadlines(paper,number):
        
        top_news = []

        if paper == 'Dainik Bhaskar':
            web_content = requests.get("https://www.bhaskar.com/coronavirus/")
            soup = BeautifulSoup(web_content.text, "html.parser")
            for a in soup.findAll('a',attrs={'class':"list_thumb"}):
                x = a.get('title')
                top_news.append(x)
        elif paper == 'Patrika':
            web_content = requests.get('https://www.patrika.com/topic/coronavirus/')
            soup = BeautifulSoup(web_content.text, "html.parser")

            top = soup.find_all('div',attrs={'class':'ctbl-text'})
            for i in top:
                top_news.append(i.text.strip())
        elif paper == 'Navbharat':
            web_content = requests.get('https://navbharattimes.indiatimes.com/coronavirus/trending/74460387.cms')
            soup = BeautifulSoup(web_content.text, "html.parser")

            top = soup.find_all('a',attrs={'class':'cor_rest_art'})
            for i in top:
                top_news.append(i.text.strip())
        elif paper == 'Amarujala':
            web_content = requests.get('https://www.amarujala.com/tags/corona-special-news?page=1')
            soup = BeautifulSoup(web_content.text, "html.parser")

            top = soup.find_all('h3')
            for i in top:
                top_news.append(i.text.strip())
                
        elif paper == 'India Today':
            web_content = requests.get('https://www.indiatoday.in/coronavirus')
            soup = BeautifulSoup(web_content.text, "html.parser")
            top = soup.find_all('h3')
            for i in top:
                top_news.append(i.text.strip())
        return top_news[:number]
                     
     #   return top_news[:number]  
    
    
    
# Front Page -----------------------------------------------------------------------       
    st.markdown("<body style='background-color:white;'><h1 style='text-align: center; color: blue;'>REAL TIME  COVID-19 ANALYSIS</h1></body>", unsafe_allow_html=True)
    img = Image.open('covid1.PNG')
    st.image(img,width=700)
    st.markdown("<body style='background-color:CornflowerBlue;'><h3 style='text-align: center; color: green;'>Helpline Number for Corona Virus : +91-11-23978046 or 1075</h3></body>", unsafe_allow_html=True)
    st.markdown("<a href='https://www.mohfw.gov.in//'><marquee>Click here for Guidelines by Health Ministry of India</marquee></a>",unsafe_allow_html=True)
    st.markdown("<body style='background-color:CornflowerBlue;'><h3 style='text-align: center; color: red;'>#INDIAFIGHTSCORONA</h3></body>", unsafe_allow_html=True)
    st.markdown("<body style='background-color:DarkTurquoise;'><h3 style='text-align: center; color: black;'>#StayHome_StaySafe</h3></body>", unsafe_allow_html=True)
    day = ['Select','Today','Yesterday','2 Days Ago']
    
    st.markdown("<body style='background-color:white;'><h1 style='text-align: center; color: green;'>SELECT ACTIVITIES FROM THE SIDEBAR 👈</h1></body>", unsafe_allow_html=True)
    activities = ["Select","Indian News Paper Headlines"]
    st.sidebar.markdown("<body style='background-color:CornflowerBlue;'><h3 style='text-align: center; color: black;'>Please Select the Activities</h3></body>", unsafe_allow_html=True)
    
    
# task 1  Newspaper
#*********************
    activity = st.sidebar.selectbox("",activities)
    if activity == activities[1]:
        st.markdown("<body style='background-color:white;'><h1 style='text-align: center; color: #a84c32;'>Covid19 Newspaper Headlines</h1></body>", unsafe_allow_html=True)
        news = ['Select','Dainik Bhaskar','Patrika', 'Navbharat', 'India Today', 'Amarujala']
        paper = st.selectbox('',news)
        if paper == 'Select':
            pass
        else:
            st.markdown("<body style='background-color:white;'><h3 style='text-align: center; color: green;'>Slide through the slider to see the COVID19 news</h3></body>", unsafe_allow_html=True)            
            number = st.slider(" ",1,15)
            headlines = paperHeadlines(paper,number)
            for i in headlines:            
                st.info(i)
    else:
            pass
    st.markdown("<body style='background-color:white;'><h3 style='text-align: center; color: RED;'>*********By Ayush kumar*******<h3></body>", unsafe_allow_html=True)
    
#main ****************************************************************************'''

if __name__== '__main__':
    main()

                
    
