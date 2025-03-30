from dotenv import load_dotenv
import cohere
import os

# Load environment variables
load_dotenv()
api_key = os.getenv('COHERE_API_KEY')

# Check if API key exists
if not api_key:
    raise ValueError("COHERE_API_KEY not found. Please check your .env file.")

co = cohere.Client(api_key)

def get_budget_insights(user_query, transactions_text):
    prompt = f"""User query: {user_query}\nTransactions list: {transactions_text}\n
    You are Budget-Baba, a financial AI assistant developed by Abhishek for the Finance Tracker. 
    Respond in a structured paragraph about financial queries, including budgeting, expense tracking, and savings advice.
    If the user asks unrelated questions, respond: "I can only assist with financial-related questions."
    """

    response = co.chat(
        model='command-xlarge-nightly',   
        message=prompt
    )

    return response.text
