import streamlit as st
from time import sleep
from streamlit_extras.app_logo import add_logo

# Initialize session state if not set
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

def make_sidebar():
    with st.sidebar:
        col1, col2, col3 = st.columns([1, 8, 1], gap="small")
        with col2:
            st.image("assets/logo.png", width=200)
        st.divider()

        if st.session_state.get("logged_in", False):
            # ✅ Sidebar Navigation with Icons
            st.page_link("pages/Sales_Overview.py", label="Sales Overview", icon="💹")
            st.page_link("pages/P&L.py", label="P&L", icon="💸")
            st.page_link("pages/Style_Review.py", label="Style Review", icon="👕")
            st.page_link("pages/Actions.py", label="Actions", icon="⏯️")
            st.page_link("pages/Data_Export.py", label="Data Export", icon="📨")
            st.page_link("pages/Data_Import.py", label="Data Import", icon="📩")
            st.page_link("pages/Data_Sync.py", label="Data Sync", icon="♾️")

            # Logout Button
            if st.button("Log out"):
                logout()

        else:
            # 🚨 If the user is not logged in, prevent access to other pages
            if "home.py" not in st.session_state.get("current_page", ""):
                st.warning("Redirecting to login page...")
                sleep(1)
                st.switch_page("home.py")

def logout():
    """Logs the user out and redirects to the home page."""
    st.session_state["logged_in"] = False
    st.info("Logged out successfully!")
    sleep(0.5)
    st.switch_page("home.py")
