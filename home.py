import streamlit as st
from time import sleep
from navigation import make_sidebar

st.set_page_config(layout="wide")
make_sidebar()

st.markdown("""
    <style>
            .block-container {
                padding-top: 1rem;
                padding-bottom: 0rem;
                padding-left: 1rem;
                padding-right: 1rem;
                    line-height: 30%;
                text-align: center;
                font-size : 15px;
                gap: 0rem;

            }
            .divder{
                padding-top: 0rem;
                padding-bottom: 0rem;
                padding-left: 0rem;
                padding-right: 0rem;
        }

            .box-font {
font-size:14px !important;

}

        .value-font {
font-size:15px !important;

}
                </style>
    """, unsafe_allow_html=True)

st.title("Welcome to 90NorthBrands")

st.write("Please log in to continue ")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Log in", type="primary"):
    if username == st.secrets["username"] and password == st.secrets["password"]:
        st.session_state.logged_in = True
        st.success("Logged in successfully!")
        sleep(0.5)
        st.switch_page("pages/Sales_Overview.py")
    else:
        st.error("Incorrect username or password")
