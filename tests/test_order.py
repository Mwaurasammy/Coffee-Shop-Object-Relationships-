from order import Order
from customer import Customer
from coffee import Coffee

def test_order_creation():
    customer = Customer("Sammy")
    coffee = Coffee("Espresso")
    order = Order(customer, coffee, 5.0)
    assert order.price == 5.0

def test_invalid_price():
    customer = Customer("Sammy")
    coffee = Coffee("Latte")
    try:
        Order(customer, coffee, 15.0)
    except ValueError as e:
        assert str(e) == "Price must be between 1.0 and 10.0."
