import sqlite3
import streamlit as st
import hashlib  # to secure the password of user
class AuthManager:

    def __init__(self, db_name="users.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

        # Create users table if not exists 
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            email TEXT UNIQUE,
                            password TEXT)''')
        self.conn.commit()

    
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()  # 'sha256' is a hashing algorithm for security purpose
    
    def register_user(self, email, password):
        try:
            hashed_pw = self.hash_password(password)
            self.cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, hashed_pw))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False    # If Email already exists
        
    
    def login_user(self, email, password):
        hashed_pw = self.hash_password(password)
        self.cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, hashed_pw))
        return self.cursor.fetchone() is not None
    