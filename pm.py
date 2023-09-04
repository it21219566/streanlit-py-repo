import streamlit as st
import pandas as pd
import numpy as np

# Create a list of products
products = pd.DataFrame({
    "Product Name": ["Fifa 19", "Glacier White 500GB", "Platinum Headset"],
    "Price": [44, 249.99, 119.99],
    "Quantity": [1, 1, 1]
})

# Create a function to display the shopping cart
def show_shopping_cart():
    st.title("Shopping Cart")
    st.table(products)
    st.markdown("Order Summary")
    st.subheader("Price")
    st.text(f"£{products['Price'].sum()}")
    st.subheader("Shipping")
    st.text("Standard Delivery - £5.00")
    st.subheader("Promo Code")
    st.text("")
    st.text("Enter code")
    st.text("")
    st.text("Apply")

# Create a function to add a product to the shopping cart
def add_product_to_cart(product_name):
    products.loc[products['Product Name'] == product_name, 'Quantity'] += 1

# Create a function to remove a product from the shopping cart
def remove_product_from_cart(product_name):
    products.loc[products['Product Name'] == product_name, 'Quantity'] -= 1

# Create a function to apply a promo code
def apply_promo_code(promo_code):
    if promo_code == "10OFF":
        products['Price'] = products['Price'] * 0.9

# Create a function to checkout
def checkout():
    st.write("Thank you for your purchase!")

# Run the Streamlit app
st.title("Shopping Cart")
show_shopping_cart()

# Add product to cart button
st.button("Add Product to Cart", key="add_product")

# Remove product from cart button
st.button("Remove Product from Cart", key="remove_product")

# Apply promo code button
st.button("Apply Promo Code", key="apply_promo_code")

# Checkout button
st.button("Checkout", key="checkout")
