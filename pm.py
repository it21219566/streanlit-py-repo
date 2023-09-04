#Core Package
import streamlit as st

#EDA Packages
import pandas as pd

def main():
    st.title("Add Item")

    menu = ["Add New Item","Item List","Update","Delete","About"]
    choice = st.sidebar.selectbox("Menu",menu)

    

if __name__ == '_main_':
    main()
