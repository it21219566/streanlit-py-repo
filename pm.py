import streamlit as st
import pandas as pd
from random import choice

st.title('Add Item')

menu = ["Add New Item","Item List","Update","Delete","About"]
choice = st.sidebar.selectbox("Menu",menu)

if choice == "Add New Item":
        st.subheadder("New Item")

elif choice == "Item List":
        st.subheader("View Items")
elif choice == "Update":
        st.subheader("Update Item")
elif choice == "Delete":
        st.subheader("Delete Item")
        
else:
        st.subheader("About")
