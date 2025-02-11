import streamlit as st
import json
import requests
import src.Space_Titanic_Preproc as sp

st.header("Titanic Prediction")
st.dataframe(sp.df)
