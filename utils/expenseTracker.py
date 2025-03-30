import sqlite3
import pandas as pd
import streamlit as st



# Income Manager class using db
class IncomeManager:

    
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

        # Create the table if it doesn't exist
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS income
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            date DATE,
                            amount REAL,
                            source TEXT,
                            description TEXT)''')
        self.conn.commit()

    def addIncome(self, date, name, amount, source, description):
        self.cursor.execute('''INSERT INTO income (name, date, amount, source, description)
                            VALUES (?, ?, ?, ?, ?)''',
                            (name, date, amount, source, description))
        self.conn.commit()

    def viewIncome(self):
        query = "SELECT * FROM income"
        return pd.read_sql(query, self.conn)
    
    def deleteIncome(self, income_id):
        self.cursor.execute("DELETE FROM income WHERE id=?", (income_id,))
        self.conn.commit()




# Expense Manager class using db
class ExpenseManager:


    def __init__(self, db_name):

        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

        # Create the table if it doesn't exist
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            date DATE,
                            amount REAL,
                            category TEXT,
                            description TEXT)''')
        self.conn.commit()

    def addExpense(self, date, name, amount, category, description):
        self.cursor.execute('''INSERT INTO expenses (name, date, amount, category, description)
                            VALUES (?, ?, ?, ?, ?)''',
                            (name, date, amount, category, description))
        self.conn.commit()

    def viewExpenses(self):
        query = "SELECT * FROM expenses"
        return pd.read_sql(query, self.conn)
    
    def deleteExpense(self, expense_id):
        self.cursor.execute("DELETE FROM expenses WHERE id=?", (expense_id,))
        self.conn.commit()





# Account class using db
class Account:
    def __init__(self, db_name):
        self.IncomeManager = IncomeManager(db_name)
        self.ExpenseManager = ExpenseManager(db_name)
        self.Balance = 0.0 

    def getBalance(self):
        # total_income = self.IncomeManager.viewIncome()["amount"].sum()
        # total_expense = self.ExpenseManager.viewExpenses()["amount"].sum()
        
        total_income = self.IncomeManager.viewIncome().get("amount", pd.Series([0])).sum()
        total_expense = self.ExpenseManager.viewExpenses().get("amount", pd.Series([0])).sum()
    
        self.Balance = total_income - total_expense 
        return self.Balance
    
    
    def addIncome(self, date, name, amount, source, description):
        self.IncomeManager.addIncome(date, name, amount, source, description)
        self.Balance += amount
        st.success(f"Income added successfully!")
    
    def addExpense(self, date, name, amount, category, description):
        self.ExpenseManager.addExpense(date, name, amount, category, description)
        self.Balance -= amount
        st.success(f"Expense added successfully!")


    def incomeList(self):
        return self.IncomeManager.viewIncome()

    def expenseList(self):
        return self.ExpenseManager.viewExpenses()
    

    def deleteIncome(self, income_id):
        incomes = self.IncomeManager.viewIncome()
        if incomes.empty:
            st.warning("No income records to delete")
            return
    
        if income_id in incomes["id"].values:
            amount = incomes.loc[incomes['id'] == income_id, "amount"].iloc[0]
            self.IncomeManager.deleteIncome(income_id)
            self.Balance -= amount
            st.success(f"Income {income_id} deleted successfully!")
        else:
            st.warning(f"Invalid Income ID: {income_id}")

    
    def deleteExpense(self, expense_id):
        expenses = self.ExpenseManager.viewExpenses()
        if expenses.empty:
            st.warning("No expenses to delete")
            return
        
        if expense_id in expenses["id"].values:
            amount = expenses.loc[expenses["id"] == expense_id, "amount"].iloc[0]
            self.ExpenseManager.deleteExpense(expense_id)
            self.Balance += amount
            st.success(f"Expense {expense_id} deleted successfully!")
        else:
            st.warning(f"Invalid Expense ID: {expense_id}")



    # transactions list
    def format_transactions_for_ai(self):
        income = self.IncomeManager.viewIncome()
        expenses = self.ExpenseManager.viewExpenses()

        formatted_income = income[['name', 'date', 'amount', 'source', 'description']].to_dict(orient='records')
        formatted_expenses = expenses[['name', 'date', 'amount', 'category', 'description']].to_dict(orient='records')

        # final dictionary to be returned
        transactions = {
            'income' : formatted_income,
            'expenses' : formatted_expenses
        }

        return transactions
    def generate_ai_insights(self):
        """Generate AI-based insights and suggestions for managing expenses."""
        transactions = self.format_transactions_for_ai()

        # Example logic for AI processing (replace this with your actual AI model)
        insights = []
        
        # 1. Analyze spending patterns
        expense_categories = {}
        for expense in transactions['expenses']:
            category = expense['category']
            amount = expense['amount']
            if category in expense_categories:
                expense_categories[category] += amount
            else:
                expense_categories[category] = amount
        
        # Suggest reducing highest spending category
        if expense_categories:
            max_category = max(expense_categories, key=expense_categories.get)
            insights.append(f"⚡ You are spending the most on '{max_category}'. Consider reducing expenses in this category.")

        # 2. Analyze income-to-expense ratio
        total_income = sum(item['amount'] for item in transactions['income'])
        total_expense = sum(item['amount'] for item in transactions['expenses'])
        
        if total_income > 0:
            expense_ratio = (total_expense / total_income) * 100
            if expense_ratio > 70:
                insights.append(f"⚠️ Your expenses are {expense_ratio:.2f}% of your income. Try to keep this below 50%.")
            else:
                insights.append(f"✅ Good job! Your expenses are under control at {expense_ratio:.2f}% of your income.")
        else:
            insights.append("❗ No income records found. Please add income data to analyze your expenses correctly.")

        # 3. Savings goal suggestion
        if total_income > 0 and total_expense > 0:
            savings = total_income - total_expense
            if savings < total_income * 0.2:
                insights.append(f"💡 Consider saving at least 20% of your income. Currently, you're saving only {savings:.2f}.")

        return insights
    
    

