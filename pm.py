import streamlit as st
import pandas as pd
import numpy as np

def load_product_data():
  """Loads the product data into a Pandas DataFrame."""
  data = pd.read_csv("products.csv")
  return data

def render_shopping_cart_page():
  """Renders the shopping cart page."""
  # Header
  st.header("Shopping Cart")

  # Search bar
  search_term = st.text_input("Search for products:")

  # Product list
  products = load_product_data()
  if search_term:
    products = products[products["name"].str.contains(search_term)]

  st.table(products)

  # Total price
  total_price = 0
  for product in products.itertuples():
    total_price += product[2]

  st.write("Total price: $", total_price)

  # Shipping and billing information
  shipping_address = st.text_input("Shipping address:")
  billing_address = st.text_input("Billing address:")

  # Order summary
  st.write("Order summary:")
  st.write("Shipping address:", shipping_address)
  st.write("Billing address:", billing_address)
  st.write("Total price: $", total_price)

  # Checkout button
  st.button("Checkout")

if __name__ == "__main__":
  render_shopping_cart_page()
