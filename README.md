# **BudgetBaba** ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)

**BudgetBaba** is a comprehensive AI-powered personal finance management application built using **Streamlit**. It helps users track their expenses, manage income, visualize spending patterns, and receive AI-powered financial insights. The application features a secure authentication system and personalized transaction management for each user.

**BudgetBaba** is a comprehensive AI-powered personal finance management application built using **Streamlit**. It helps users track their expenses, manage income, visualize spending patterns, and receive AI-powered financial insights. The application features a secure authentication system and personalized transaction management for each user.

## **Key Features**
- **🔐 Secure Authentication:** User registration and login system for personalized finance tracking
- **💰 Transaction Management:** 
  - Easy income and expense logging with categorization
  - Real-time balance tracking
  - Transaction history with delete functionality
- **📊 Financial Analytics:**
  - Interactive data visualization using Matplotlib and Seaborn
  - Spending pattern analysis
  - Category-wise expense breakdown
- **🤖 AI-Powered Insights:**
  - Smart financial suggestions
  - Spending pattern analysis
  - Personalized budget recommendations

## **Tech Stack**
- **Frontend:** Streamlit
- **Backend:** Python, SQLite
- **Data Processing:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn, Plotly
- **AI/ML:** Scikit-learn for insights generation

## **🔧 Installation & Setup**

### **Environment Variables Setup**
1. Create a `.env` file in the project root directory
2. Add your Cohort API key:
   ```
   COHORT_API_KEY=your_api_key_here
   ```
3. To obtain your API key:
   - Visit [Cohort API Dashboard](https://cohortapi.com)
   - Sign up for an account
   - Navigate to API Keys section
   - Generate a new key and copy it
   - Paste it in your `.env` file

⚠️ **Important**: Never commit your `.env` file to version control!

## **Installation**
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/BudgetBaba.git
   cd BudgetBaba
   ```

2. **Set up Python virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the application:**
   ```bash
   streamlit run Home.py
   ```

## **Usage Guide**
1. **Getting Started:**
   - Register a new account or login with existing credentials
   - Navigate through features using the sidebar

2. **Managing Transactions:**
   - Log new income and expenses with categories
   - Add transaction details including date, amount, and description
   - View and manage transaction history

3. **Analyzing Finances:**
   - View interactive charts and reports
   - Get AI-powered insights about spending patterns
   - Track budget progress and financial goals

## **Contributing**
We welcome contributions! Here's how you can help:
1. Fork the repository
2. Create your feature branch: `git checkout -b feature/AmazingFeature`
3. Commit your changes: `git commit -m 'Add some AmazingFeature'`
4. Push to the branch: `git push origin feature/AmazingFeature`
5. Open a Pull Request

## **📜 License**
This project is licensed under the BSD 2-Clause License - see the `LICENSE` file for details.

---

✨ **BudgetBaba - Your AI-Powered Financial Companion** 💰 ✨

![Finance Dashboard](https://via.placeholder.com/800x400.png?text=BudgetBaba+Dashboard+Preview)

