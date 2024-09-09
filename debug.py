from customer import Customer
from coffee import Coffee
from order import Order

def debug_customer():
    print("\n--- Debugging Customer ---")
    name = input("Enter customer name: ")
    customer = Customer(name)
    print(f"Customer created: {customer.name}")
    return customer

def debug_coffee():
    print("\n--- Debugging Coffee ---")
    coffee_name = input("Enter coffee type: ")
    coffee = Coffee(coffee_name)
    print(f"Coffee created: {coffee.name}")
    return coffee

def debug_order():
    print("\n--- Debugging Order ---")
    customer = debug_customer()
    coffee = debug_coffee()
    price = float(input("Enter coffee price: "))
    
    order = Order(customer, coffee, price)
    print(f"Order placed successfully: {customer.name} ordered a {coffee.name} for ${price:.2f}.")
    return order

def main():
    while True:
        print("\nSelect an option to debug:")
        print("1. Customer")
        print("2. Coffee")
        print("3. Order")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            debug_customer()
        elif choice == '2':
            debug_coffee()
        elif choice == '3':
            debug_order()
        elif choice == '4':
            print("Exiting debug mode.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
