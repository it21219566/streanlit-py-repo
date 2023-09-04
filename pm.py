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

    menu = ["Your Cart", "Shipping", "Billing", "Order Summary"]
    choice = st.sidebar.selectbox("Menu", menu)

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
        st.subheader("Shipping Address")

        # Create a shipping details form
        with st.form("shipping_details_form"):
            col1, col2 = st.columns(2)  # Create two columns here

            with col1:
                first_name = st.text_input("First Name")

            with col2:
                last_name = st.text_input("Last Name")

            address = st.text_area("Address")
            email = st.text_input("Email")
            phone = st.text_input("Phone")

            submitted = st.form_submit_button("Submit Shipping Details")

        if submitted:
            # Need to store the shipping details in a dictionary or a database...
            shipping_details = {
                "First Name": first_name,
                "Last Name": last_name,
                "Address": address,
                "Email": email,
                "Phone": phone,
            }
            st.success("Shipping details submitted successfully!")
            # Need to redirect to the next step (e.g., Billing)...

    elif choice == "Billing":
        st.subheader("Billing Address")

        # Billing Details form
        with st.form("billing_details_form"):
            col1, col2 = st.columns(2)  # Create two columns here

            with col1:
                first_name = st.text_input("First Name")

            with col2:
                last_name = st.text_input("Last Name")

            address = st.text_area("Address")
            email = st.text_input("Email")
            phone = st.text_input("Phone")

            submitted = st.form_submit_button("Submit Billing Details")

        if submitted:
            # Need to store the billing details in a dictionary or a database...
            billing_details = {
                "First Name": first_name,
                "Last Name": last_name,
                "Address": address,
                "Email": email,
                "Phone": phone,
            }
            st.success("Billing details submitted successfully!")

        st.subheader("Payment Details")
        # Payment details form
        with st.form("payment_details_form"):
            # Create a payment details form
            credit_card_number = st.text_input("Credit Card Number")
            expiration_date = st.text_input("Expiration Date (MM/YY)")
            cvv = st.number_input("CVV", min_value=0, step=1)

            submitted = st.form_submit_button("Submit Payment Details")

            if submitted:
                # Need to store the payment details in a secure manner...
                payment_details = {
                    "Credit Card Number": credit_card_number,
                    "Expiration Date": expiration_date,
                    "CVV": cvv,
                }
                st.success("Payment details submitted successfully!")
                # Need to process the payment...

    else:
        st.subheader("Order Summary")

if __name__ == "__main__":
    main()
