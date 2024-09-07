from coffee import Coffee
from customer import Customer
from order import Order

def test_coffee_creation():
    coffee = Coffee("Latte")
    assert coffee.name == "Latte"

def test_invalid_coffee_name():
    try:
        Coffee("Lo")
    except ValueError as e:
        assert str(e) == "Coffee name must be at least 3 characters."

def test_num_orders():
    customer = Customer("Rin")
    coffee = Coffee("Cappuccino")
    customer.create_order(coffee, 3.0)
    assert coffee.num_orders() == 1
