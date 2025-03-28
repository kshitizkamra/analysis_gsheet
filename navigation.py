import streamlit as st
from time import sleep
from streamlit_extras.app_logo import add_logo

def get_current_page_name():
    # Streamlit doesn't provide a built-in way to get the current page name in recent versions.
    # You might need to manually track this if required or rely on session state.
    return st.session_state.get("current_page", "home")

def make_sidebar():
    with st.sidebar:
        col1, col2, col3 = st.columns([1, 8, 1], gap="small")
        with col2:
            st.image("assets/logo.png", width=200)
        st.divider()

        if st.session_state.get("logged_in", False):
            st.markdown("### Navigation")
            st.markdown("[💹 Sales Overview](./Sales_Overview)")
            st.markdown("[💸 P&L](./P&L)")
            st.markdown("[👕 Style Review](./Style_Review)")
            st.markdown("[⏯️ Actions](./Actions)")
            st.markdown("[📨 Data Export](./Data_Export)")
            st.markdown("[📩 Data Import](./Data_Import)")
            st.markdown("[♾️ Data Sync](./Data_Sync)")

            if st.button("Log out"):
                logout()
            st.divider()
        elif get_current_page_name() != "home":
            # If user is not logged in, redirect to home page
            st.warning("Redirecting to login...")
            sleep(1)
            st.experimental_rerun()

def logout():
    st.session_state["logged_in"] = False
    st.info("Logged out successfully!")
    sleep(0.5)
    st.experimental_rerun()
