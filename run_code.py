from customer import Customer
from coffee import Coffee
from order import Order

def run():
    print("Welcome to the Coffee Shop!\n")

    # Get customer name
    customer_name = input("Please enter your name: ")
    customer = Customer(customer_name)

    # List available coffee types
    coffee_menu = {
        1: "Espresso",
        2: "Latte",
        3: "Cappuccino",
        4: "Americano",
        5: "Mocha"
    }

    print("\nAvailable Coffees:")
    for number, coffee_name in coffee_menu.items():
        print(f"{number}: {coffee_name}")

    # Get coffee choice
    try:
        coffee_choice = int(input("\nPlease choose a coffee (enter number): "))
        if coffee_choice not in coffee_menu:
            raise ValueError("Invalid coffee choice.")
        coffee = Coffee(coffee_menu[coffee_choice])
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Get the price
    try:
        price = float(input("Enter the price of the coffee (between 1.0 and 10.0): "))
        if price < 1.0 or price > 10.0:
            raise ValueError("Price must be between 1.0 and 10.0.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Create the order
    try:
        order = Order(customer, coffee, price)
        print(f"\nOrder successfully created for {order.customer.name}!")
        print(f"Coffee: {order.coffee.name}, Price: ${order.price:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run()
