import streamlit as st
import sqlite3
import time
from utils.expenseTracker import ExpenseManager
from utils.expenseTracker import IncomeManager
from utils.expenseTracker import Account
from Authentication import AuthManager

st.title("Budget-Baba")
st.write("An AI powered finance tracker")

auth = AuthManager()

# Session state for tracking login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_email = ""


tab1, tab2 = st.tabs(["🔑 Login", "📝 Register"])

with tab1:
    st.subheader("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        if auth.login_user(email, password):
            st.session_state.logged_in = True
            st.session_state.user_email = email
            st.success("Login successful!! Redirecting...")
        else:
            st.error("Invalid email or password")
    
with tab2:
    st.subheader("Register")
    new_email = st.text_input("New Eamil")
    new_password = st.text_input("New Password", type="password")
    register_button = st.button("Register")

    if register_button:
        if auth.register_user(new_email, new_password):
            st.success("Registration successful! Please log in.")
        else:
            st.error("Email alredy exists")

# Check if the user is logged in 
if st.session_state.logged_in:
    st.success("Head to side bar to user features")


# Dynamically set the database name
db_name = "expense.db"

# Initialize the managers with the database name
ExManager = ExpenseManager(db_name=db_name)
InManager = IncomeManager(db_name=db_name)
account = Account(db_name=db_name)

# Establhish SQLite databse connection for testing 
conn = sqlite3.connect(db_name)
c = conn.cursor()

if st.session_state.logged_in:

    # Toast notification
    st.toast("Welcome to Budget-Baba!💰")

conn.close()
