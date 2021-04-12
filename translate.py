# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 12:10:45 2021

@author: jkran
"""

#setup the google api, the main version didnt work for me so I used an alternate
from google_trans_new import google_translator  
translator = google_translator()  

#the function that translates
def translate(text):    
    return translator.translate(text,lang_tgt='fr')  

    
