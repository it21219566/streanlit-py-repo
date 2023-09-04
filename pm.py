import streamlit as st
import pandas as pd

st.title('Add Item')

menu = ["Add New Item","Item List","Update","Delete","About"]
choice = st.sidebar.selectbox("Menu",menu)
