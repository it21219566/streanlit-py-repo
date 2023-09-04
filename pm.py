import streamlit as st

# Create a dictionary to store product information
products = {
    'Product 1': 10.00,
    'Product 2': 15.00,
    'Product 3': 20.00,
}

# Initialize an empty cart
cart = {}

# Streamlit app
def main():
    st.title("Shopping Cart Web App")
    st.write("## Welcome to the Shopping Cart Web App")
    st.write("Browse products on the left sidebar and add them to your cart.")

    menu = ["Your Cart","Shipping","Billing","Order Summary"]
    choice = st.sidebar.selectbox("Menu",menu)

    selected_product = st.selectbox("Select a product:", list(products.keys()))
    quantity = st.number_input("Quantity:", 1, 100, 1)

    if st.button("Add to Cart"):
        if selected_product in cart:
            cart[selected_product] += quantity
        else:
            cart[selected_product] = quantity

    if st.button("Clear Cart"):
        cart.clear()

    st.write("### Cart")
    for product, qty in cart.items():
        st.write(f"{product}: {qty} items")

    total_cost = sum(products[product] * qty for product, qty in cart.items())
    st.write(f"**Total Cost: ${total_cost:.2f}**")

if __name__ == "__main__":
    main()
