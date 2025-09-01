#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self._size = None
        self.size = size # Triggers setter validation
        self.price = price

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        allowed_sizes = ["Small", "Medium", "Large"]
        if value in allowed_sizes:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1 # Increases the price by 1
