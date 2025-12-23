import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

st.title("AI Budget Planner 💰")

# Input
income = st.number_input("Monthly Income (₹)", min_value=0, step=500)
st.subheader("Monthly Expenses")
rent = st.number_input("Rent", min_value=0, step=100)
food = st.number_input("Food", min_value=0, step=100)
entertainment = st.number_input("Entertainment", min_value=0, step=100)

if st.button("Analyze Budget"):
    expenses = {"rent": rent, "food": food, "entertainment": entertainment}
    data = {"income": income, "expenses": expenses}
    
    # Call Flask API
    response = requests.post("http://127.0.0.1:5000/api/analyze", json=data)
    result = response.json()
    
    st.write("### Budget Summary")
    st.write(result)
    
    # Visualization
    categories = list(result["categories"].keys())
    amounts = list(result["categories"].values())
    
    fig, ax = plt.subplots()
    ax.pie(amounts, labels=categories, autopct="%1.1f%%")
    st.pyplot(fig)
