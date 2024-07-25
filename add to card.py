# List of predefined email and password pairs (for demonstration)
registered_users = {
    'user1@example.com': 'password1',
    'user2@example.com': 'password2'
}

# Decorator function to check if user is authenticated
def login_required(func):
    def wrapper(*args, **kwargs):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        
        if (email in registered_users) and (registered_users[email] == password):
            print("Authentication successful!")
            func(*args, **kwargs)
        else:
            print("Authentication failed.")
            create_account = input("Would you like to create an account? (yes/no): ").lower()
            if create_account == 'yes':
                new_email = input("Enter your email: ")
                new_password = input("Enter your password: ")
                registered_users[new_email] = new_password
                print(f"Account created successfully for {new_email}!")
                func(*args, **kwargs)  # Proceed with adding to cart after account creation
            else:
                print("Not adding to cart. Goodbye!")
    
    return wrapper

# Function to add item to cart
@login_required
def add_to_cart(product_name, price, quantity, subtotal):
    print(f"Adding {quantity} of {product_name} to cart.")
    print(f"Price per item: ${price}")
    print(f"Total cost: ${subtotal}")

# Example usage
if __name__ == "__main__":
    # Example of adding to cart
    add_to_cart("Laptop", 1500.0, 1, 1500.0)
