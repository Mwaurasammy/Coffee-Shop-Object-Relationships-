class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []   #list for orders
        
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Customer name must be a string.")
        if not (1 <= len(value) <= 15):
            raise ValueError("Customer name must be between 1 and 15 characters.")
        self._name = value
        
    def orders(self):  #return all orders
        return self._orders
    
    def coffees(self):     #return all coffees ordered by customer
        return list(set([order.coffee for order in self._orders]))
    
    
    def create_order(self, coffee, price):  #create order
        from order import Order
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee._orders.append(order)