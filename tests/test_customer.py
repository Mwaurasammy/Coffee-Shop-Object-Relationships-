from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_creation():
    customer = Customer("Sammy")
    assert customer.name == "Sammy"
    
def test_invalid_customer_name():
    try:
        Customer("ThisNameIsTooLong")
    except ValueError as e:
        assert str(e) == "Customer name must be between 1 and 15 characters."
        
def test_create_order():
    customer = Customer("Rin")
    coffee = Coffee("Espresso")
    customer.create_order(coffee, 5.0)
    assert len(customer.orders()) == 1
    assert coffee in customer.coffees()