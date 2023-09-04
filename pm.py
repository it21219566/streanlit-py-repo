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

        # Create a shipping details form
        with st.form("shipping_details_form"):
            col1, col2 = st.columns(2)
            with col1:
                first_name = st.text_input("First Name")
            with col2:
                last_name = st.text_input("Last Name")

            address = st.text_area("Address")
            email = st.text_input("Email")
            phone = st.text_input("Phone")

            submitted = st.form_submit_button("Submit Shipping Details")

        if submitted:
            # Need to store the shipping details in a dictionary or a database......
            shipping_details = {
                "First Name": first_name,
                "Last Name": last_name,
                "Address": address,
                "Email": email,
                "Phone": phone,
            }
            st.success("Shipping details submitted successfully!")
            # Need to redirect to the next step (e.g., Billing)......
        
    elif choice == "Billing":
        st.subheader("Billing")

    else:
        st.subheader("Oreder Summery")
    
if __name__ == "__main__":
    main()
