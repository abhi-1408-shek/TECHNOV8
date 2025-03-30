import streamlit as st
from utils.expenseTracker import Account
import time

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please log in to continue : ")
    st.stop()

user_email = st.session_state.user_email
db_name = f"{user_email}.db"
account = Account(db_name=db_name)




st.title("💵 Log Transactions")
st.divider()
if "balance" not in st.session_state:
    st.session_state.balance = account.getBalance()     # fetch from database


formatted_balance = f"₹{st.session_state.balance:.2f}"
st.write(f"Current Balance : {formatted_balance}")


# Add Income
with st.expander("⬇ Add New Income"):
    with st.form("income_form"):
        inName = st.text_input("Income Title")
        inDate = st.date_input("Income Date")
        inAmount = st.number_input("Amount Received", min_value=0.0)
        inDescription = st.text_area("Description")
        inSource = st.selectbox("Source of Income", ("-","Salary 💳", "Family 👨 ", "Investment 💱", "Other"))
        submit_income = st.form_submit_button("Add Income ➕")

        if submit_income:
            account.addIncome(inDate, inName, inAmount, inSource, inDescription)
            st.session_state.balance += inAmount    # Add to balance
            st.toast("✅ Income Added Successfully!!!")
            time.sleep(1.5)     # delay for 1.5 seconds
            st.rerun()


# Add Expense 
with st.expander("⬆ Add New Expense"):
    with st.form("expense_form"):
        exName = st.text_input("Expense Title")
        exDate = st.date_input("Date of Expense")
        exAmount = st.number_input("Amount Spent", min_value=0.0)
        exDescription = st.text_area("Description")
        exCategory = st.selectbox("Category of Expense", ("-","Food 🍕", "Personal 👨 ", "Transport 🚌", "Investment 💱"))
        submit_expense = st.form_submit_button("Add Expense ➕")

        if submit_expense:
            account.addExpense(exDate, exName, exAmount, exCategory, exDescription)
            st.session_state.balance -= exAmount    # Deduct from balance
            st.toast("✅ Expense Added Successfully!!!")
            time.sleep(1.5)        # delay for 1.5 seconds
            st.rerun()

