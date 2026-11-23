class GroceryItem:                     
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def line_total(self):
        return self.price * self.quantity


class Cart:
    def __init__(self):
        self.items = []

    def add(self, name, price):
        for item in self.items:
            if item.name == name:
                item.quantity += 1
                return
        self.items.append(GroceryItem(name, price))

    def remove(self, item):
        item.quantity -= 1
        if item.quantity <= 0:
            self.items.remove(item)

    def total(self):
        return sum(item.line_total() for item in self.items)


def make_receipt(cart, tax_rate=0.25):
    lines = []
    lines.append(f"{'Netto 2.0 Kvittering':^40}")      
    lines.append("-" * 40)
    lines.append(f"{'Item':<18}{'Qty':>4}{'Price':>9}{'Total':>9}")

    subtotal = 0.0
    for item in cart.items:                           
        total = item.line_total()
        subtotal += total
        lines.append(f"{item.name[:18]:<18}{item.quantity:>4}{item.price:>9.2f}{total:>9.2f}")

    moms = subtotal * tax_rate / (1 + tax_rate)   # 25% moms = 20% of a price that already includes it
    lines.append("-" * 40)
    lines.append(f"{'TOTAL':<31}{subtotal:>9.2f}")
    lines.append(f"{'Heraf moms':<31}{moms:>9.2f}")
    return lines


def purchase(cart):
    if not cart.items:                 
        print("Cart is empty.")
        return None
    receipt = make_receipt(cart)
    for line in receipt:
        print(line)
    cart.items.clear()
    return receipt

if __name__ == "__main__":
    cart = Cart()
    cart.add("Milk", 12.95)
    cart.add("Milk", 12.95)
    cart.add("Rugbrød", 22.00)
    purchase(cart)


