#!/usr/bin/env python3

class CashRegister:
  def __init__(self,discount = 0):
    self.discount = discount
    self.items = []
    self.total = 0
    self.last_transaction = 0

  def add_item(self,title,price,quantity=1):
    self.total += price * quantity
    self.last_transaction = price*quantity
    for i in range(quantity):
      self.items.append(title)

  def apply_discount(self):
    if self.discount > 0:
      client_discount = self.total * (self.discount/100) 
      self.total -= client_discount
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")
    
  def void_last_transaction(self):
    self.total -= self.last_transaction
    self.last_transaction = 0

  




    
