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
    st.title("Shopping Cart")

    st.sidebar.header("Products")
    selected_product = st.sidebar.selectbox("Select a product:", list(products.keys()))
    quantity = st.sidebar.number_input("Quantity:", 1, 100, 1)

    if st.sidebar.button("Add to Cart"):
        if selected_product in cart:
            cart[selected_product] += quantity
        else:
            cart[selected_product] = quantity

    if st.sidebar.button("Clear Cart"):
        cart.clear()

    st.sidebar.header("Cart")
    for product, qty in cart.items():
        st.sidebar.write(f"{product}: {qty} items")

    total_cost = sum(products[product] * qty for product, qty in cart.items())
    st.sidebar.subheader(f"Total Cost: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
