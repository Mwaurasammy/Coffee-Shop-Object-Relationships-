class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders = []  #list for orders
        
        
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Coffee name must be a string.")
        if len(value) < 3:
            raise ValueError("Coffee name must be at least 3 characters.")
        self._name = value
        
        
    def orders(self):   #return all orders for this coffee
        return self._orders

    def customers(self):
        return list(set([order.customer for order in self._orders]))
    
    def num_orders(self):  #number of orders for this coffee
        return len(self._orders)
    
    def average_price(self):
        if not self._orders:
            return 0
        return sum([order.price for order in self._orders]) / len(self._orders)
    