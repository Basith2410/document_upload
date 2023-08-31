# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 10:24:38 2023

@author: Mars
"""

import streamlit as st
import pandas as pd
import PyPDF2

def main():
    st.title("PDF Data Autofill App")
    
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    
    if uploaded_file is not None:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        page = pdf_reader.pages[0]
        
        pdf_text = page.extract_text()
        
        # Assume extracted values are in a dictionary
        extracted_values = {
            "Column1": "Value1",
            "Column2": "Value2",
            "Column3": "Value3"
        }
        
        st.subheader("Extracted Values")
        st.write(extracted_values)
        
        df = pd.DataFrame([extracted_values])
        st.subheader("Autofilled DataFrame")
        st.write(df)

if __name__ == "__main__":
    main()
