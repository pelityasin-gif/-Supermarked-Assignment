import pygame
import os
from time import sleep


class GroceryItem:
        def _init__(self, name, price):
                self.name = name
                self.price = price

Banana = GroceryItem("Banana", 2.5)
Spaghetti = GroceryItem("Spaghetti", 12.0)
Tomato = GroceryItem("Tomato", 3.5)
Beef = GroceryItem("Beef", 84.95)
Candy = GroceryItem("Candy", 20.0)
Pringles = GroceryItem("Pringles", 15.0)
FaxeKondi = GroceryItem("Faxe Kondi", 23.0)
Milk = GroceryItem("Milk", 13.0)
Cucumber = GroceryItem("Cucumber", 10.0)
Condoms = GroceryItem("Condoms", 30.0)

def main():
        # Create a list of all the items in the store
        items = []

        # Create an empty shopping cart
        cart = []

        # Show the items and ask the user which item they want to choose
        # item_name = input("Which item would you like to choose? ")

        # Ask how many of the item the user wants to buy (1-10)
        # quantity = int(input("How many would you like to buy? "))

        # Find the item and add it to the shopping cart
        # add_to_cart(items, item_name, quantity)

        # Repeat item selection until the user is finished shopping

        # Calculate the total price
        total_price = calculate_total_price(cart)

        # Show the receipt
        # receipt_grocery(cart)

        # Ask the user to pay the total
        payment_method(total_price)

def calculate_total_price(items):
        total_price = 0
        for item in items:
                total_price += item.price
        return total_price

def add_to_cart(items, item_name, quantity):
    for item in items:
        if item.name == item_name:
            print("How many of this item would you like to add to your shopping cart? (1-10)")
            print(f"Your shopping cart now contains: {quantity} {item.name} for {item.price * quantity} DKK.")
            break




# Item selection is handled in main().

def payment_method(total_price):
        print("How would you like to pay? (Cash, Card, MobilePay)")
        payment_method = input()
        if payment_method == "Cash":
                print("You have chosen to pay with cash.")
                cash_amount = float(input("Please enter the amount of cash you are paying: "))
                if cash_amount >= total_price:
                        print("Thank you for your payment.")
                        change = cash_amount - total_price
                        print(f"Your change is {change} DKK.")
                else: 
                        print("Insufficient cash. Please try again.")
                        return      
        elif payment_method == "Card":
                print("You have chosen to pay with card.")
                sleep(4)
                os.system("cls" if os.name == "nt" else "clear")
                print("Thank you for your payment.")
        else:
                print("Invalid payment method. Please choose again.")
                return

def receipt_grocery(items, quantity):
        print("Receipt:")
        for item in items:
                print(f"{item.name}: {item.price}: {quantity} DKK")
        print(f"Total price: {calculate_total_price(items)} DKK")
