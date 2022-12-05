import streamlit as st

title = st.text_input("Search:", "")
st.write("You search for: ", title)


import time

with st.empty():
     for seconds in range(60):
         st.write(f"⏳ {seconds} seconds have passed")
         time.sleep(1)
     st.write("✔️ 1 minute over!")

     