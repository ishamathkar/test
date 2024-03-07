import streamlit as st

email=st.text_input("Enter Email")
password=st.text_input("Enter Password")

btn=st.button("Login")

if btn:
    if email == "amangupta@gmail.com" and password =="12345":
        st.balloons()
    else:
        st.error("Your email id or password is incorrect")
