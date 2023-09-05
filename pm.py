import streamlit as st
import sqlite3

# Create a SQLite database or connect to an existing one
conn = sqlite3.connect("shopping_cart.db")
cursor = conn.cursor()

# Create a Products table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price REAL
    )
""")

# Create a Cart table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS cart (
        id INTEGER PRIMARY KEY,
        product_id INTEGER,
        quantity INTEGER
    )
""")

# Function to add a product to the cart
def add_to_cart(product_id, quantity):
    cursor.execute("INSERT INTO cart (product_id, quantity) VALUES (?, ?)", (product_id, quantity))
    conn.commit()

# Function to retrieve all products
def get_products():
    cursor.execute("SELECT * FROM products")
    return cursor.fetchall()

# Function to retrieve items in the cart
def get_cart_items():
    cursor.execute("""
        SELECT cart.id, products.name, products.price, cart.quantity
        FROM cart
        INNER JOIN products ON cart.product_id = products.id
    """)
    return cursor.fetchall()

# Function to clear the cart
def clear_cart():
    cursor.execute("DELETE FROM cart")
    conn.commit()

# Streamlit app
def main():
    st.title("Shopping Cart")
    st.write("## Welcome to the Shopping Cart")

    menu = ["Your Cart", "Shipping", "Billing", "Order Summary"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Your Cart":
        st.subheader("Your Cart")
        st.write("Manage your cart, Add or remove products from the cart.")

        # Add products to the database (you can customize this)
        if st.button("Add Sample Products"):
            cursor.executemany("INSERT INTO products (name, price) VALUES (?, ?)", [("Product 1", 10.0), ("Product 2", 15.0)])
            conn.commit()

        # Display available products
        st.subheader("Available Products")
        products = get_products()
        for product in products:
            product_id, name, price = product
            if st.button(f"Add to Cart: {name} - ${price}", key=f"add_to_cart_{product_id}"):
                quantity = st.number_input(f"Quantity for {name}", min_value=1, value=1)
                add_to_cart(product_id, quantity)

        st.write("### Cart")
        cart_items = get_cart_items()
        for cart_item in cart_items:
            cart_id, name, price, quantity = cart_item
            st.write(f"{name}: {quantity} items")

        total_cost = sum(price * quantity for _, _, price, quantity in cart_items)
        st.write(f"**Total Cost: ${total_cost:.2f}**")

        # Add a button to clear the cart
        if st.button("Clear Cart"):
            clear_cart()
            st.success("Cart has been cleared.")

    elif choice == "Shipping":
        st.subheader("Shipping Address")

        # Create a shipping details form
        with st.form("shipping_details_form"):
            col1, col2 = st.columns(2)  # Create two columns here

            with col1:
                shipping_first_name = st.text_input("First Name")

            with col2:
                shipping_last_name = st.text_input("Last Name")

            shipping_address = st.text_area("Address")
            shipping_email = st.text_input("Email")
            shipping_phone = st.text_input("Phone")

            submitted = st.form_submit_button("Submit Shipping Details")

        if submitted:
            # Need to store the shipping details in a dictionary or a database...
            shipping_details = {
                "First Name": shipping_first_name,
                "Last Name": shipping_last_name,
                "Address": shipping_address,
                "Email": shipping_email,
                "Phone": shipping_phone,
            }
            st.success("Shipping details submitted successfully!")
            # Need to redirect to the next step (e.g., Billing)...

    # Add similar code for Billing and Order Summary sections

if __name__ == "__main__":
    main()
