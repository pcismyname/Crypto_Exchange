import streamlit as st
import requests
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import plotly.express as px


API_CRYPTO = "http://localhost:8002/api/v1"

'''
Dashboard
'''

def add_cryptocurrency(name, symbol):
    """Sends a POST request to add a new cryptocurrency."""
    url = f"{API_CRYPTO}/cryptocurrencies"
    payload = {
        "name": name,
        "symbol": symbol
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        st.success("Cryptocurrency added successfully!")
    else:
        st.error(f"Failed to add cryptocurrency. Status code: {response.status_code}")

def render_add_cryptocurrency_form():
    """Renders a form to add a new cryptocurrency and handles the form submission."""
    with st.form("add_crypto_form"):
        st.write("### Add a New Cryptocurrency")
        name = st.text_input("Cryptocurrency Name", placeholder="Enter the name")
        symbol = st.text_input("Cryptocurrency Symbol", placeholder="Enter the symbol")
        submit_button = st.form_submit_button("Add Cryptocurrency")

        if submit_button and name and symbol:
            add_cryptocurrency(name, symbol)


def fetch_cryptocurrencies():
    """Fetches the list of cryptocurrencies and their inventory from the API."""
    response = requests.get(f"{API_CRYPTO}/cryptocurrencies")
    if response.status_code == 200:
        cryptos = response.json()
        for crypto in cryptos:
            # Fetch inventory for each cryptocurrency
            inventory_response = requests.get(f"{API_CRYPTO}/inventory/{crypto['crypto_id']}")
            if inventory_response.status_code == 200:
                inventory_data = inventory_response.json()
                crypto.update({
                    'total_amount': inventory_data['total_amount'],
                    'reserved_amount': inventory_data['reserved_amount']
                })
            else:
                crypto.update({'total_amount': 'N/A', 'reserved_amount': 'N/A'})
        return pd.DataFrame(cryptos)
    else:
        st.error("Failed to fetch cryptocurrencies")
        return pd.DataFrame()
    
def update_inventory(crypto_id, total_amount, reserved_amount):
    """Sends a PUT request to update cryptocurrency inventory."""
    url = f"{API_CRYPTO}/inventory/{crypto_id}"
    payload = {
        "crypto_id": crypto_id,
        "total_amount": total_amount,
        "reserved_amount": reserved_amount
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.put(url, json=payload, headers=headers)
    if response.status_code == 200:
        st.success("Inventory updated successfully!")
    else:
        st.error(f"Failed to update inventory. Status code: {response.status_code}, Error: {response.text}")

def render_update_inventory_form():
    """Renders a form to update cryptocurrency inventory and handles the form submission."""
    with st.form("update_inventory_form"):
        st.write("### Update Cryptocurrency Inventory")
        crypto_id = st.number_input("Cryptocurrency ID", min_value=1, format="%d")
        total_amount = st.number_input("Total Amount", min_value=0.0, format="%f")
        reserved_amount = st.number_input("Reserved Amount", min_value=0.0, format="%f")
        submit_button = st.form_submit_button("Update Inventory")

        if submit_button:
            update_inventory(crypto_id, total_amount, reserved_amount)



def display_cryptocurrencies():
    """Displays cryptocurrencies and their inventory in a Streamlit app using Plotly charts."""
    df = fetch_cryptocurrencies()
    if not df.empty:
        st.write("Cryptocurrencies:", df)
        # Iterate through each cryptocurrency and display its inventory as an interactive pie chart
        for index, row in df.iterrows():
            st.subheader(f"{row['name']} ({row['symbol']}) Inventory")
            st.write("Total Amount:", row['total_amount'])
            st.write("Reserved Amount:", row['reserved_amount'])

            # Only proceed if the total_amount is valid
            if row['total_amount'] != 'N/A':
                chart_data = pd.DataFrame({
                    'Amount': [row['total_amount'], row['reserved_amount']],
                    'Category': ['Available', 'Reserved']
                })
                
                # Create the pie chart using Plotly Express
                fig = px.pie(
                    chart_data,
                    values='Amount',
                    names='Category',
                    title='Inventory Distribution',
                    hole=.3,
                    color_discrete_sequence=px.colors.sequential.RdBu
                )
                fig.update_traces(textinfo='percent+label')
                st.plotly_chart(fig)
    else:
        st.write("No data available.")

def delete_cryptocurrency(crypto_id):
    """Sends a DELETE request to remove a cryptocurrency."""
    url = f"{API_CRYPTO}/cryptocurrencies/{crypto_id}"
    response = requests.delete(url)
    if response.status_code == 204:
        st.success("Cryptocurrency deleted successfully!")
    else:
        st.error(f"Failed to delete cryptocurrency. Status code: {response.status_code}, Error: {response.text}")

def render_delete_cryptocurrency_form():
    """Renders a form to delete a cryptocurrency and handles the form submission."""
    with st.form("delete_cryptocurrency_form"):
        st.write("### Delete Cryptocurrency")
        crypto_id = st.number_input("Enter Cryptocurrency ID to Delete", min_value=1, format="%d")
        submit_button = st.form_submit_button("Delete Cryptocurrency")

        if submit_button:
            delete_cryptocurrency(crypto_id)

# More functions for CREATE, UPDATE, DELETE will be added here
st.sidebar.title("Cryptocurrency Dashboard")
option = st.sidebar.selectbox(
    "Choose an action",
    ('View Cryptocurrencies', 'Add Cryptocurrency', 'Update Inventory', 'Delete Cryptocurrency')
)

if option == 'View Cryptocurrencies':
    display_cryptocurrencies()
elif option == 'Add Cryptocurrency':
    # Code for adding a cryptocurrency will go here
    render_add_cryptocurrency_form()
elif option == 'Update Inventory':
    # Code for updating a cryptocurrency will go here
    render_update_inventory_form()
elif option == 'Delete Cryptocurrency':
    # Code for deleting a cryptocurrency will go here
    render_delete_cryptocurrency_form()