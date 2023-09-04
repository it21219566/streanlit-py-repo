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
    st.write("## Welcome to the Shopping Cart")

    menu = ["Your Cart","Shipping","Billing","Order Summary"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Your Cart":
        st.subheader("Your Cart")
        st.write("Manage your cart, Add or remove products from the cart.")

        selected_product = st.selectbox("Select a product:", list(products.keys()))
        quantity = st.slider("Quantity:", 0, 100, 50)
        st.write(f'Quantity {quantity}')

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

    elif choice == "Shipping":
        st.subheader("Shipping")
        
    elif choice == "Billing":
        st.subheader("Billing")

    else:
        st.subheader("Oreder Summery")
    
if __name__ == "__main__":
    main()
