# Part A — Spot the Bug

def add_item(item, cart=[]):

    cart.append(item)
    return cart


print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", cart=["bread"]))
print(add_item("eggs"))


# Part B — Fix It
def add_item_fixed(item, cart=None):

    if cart is None:
        cart = []

    cart.append(item)
    return cart


print("\nFixed Function")

print(add_item_fixed("apple"))
print(add_item_fixed("banana"))


# Part C — Build the Cart

def create_cart(owner, discount=0):

    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }


def add_to_cart(cart, name, price, qty=1):

    cart["items"].append({
        "name": name,
        "price": price,
        "qty": qty
    })


def update_price(price_tuple, new_price):

    # Tuples are immutable, so values cannot be changed

    price_tuple[0] = new_price


def calculate_total(cart):

    total = 0

    for item in cart["items"]:

        total = total + (item["price"] * item["qty"])

    discount_amount = total * cart["discount"] / 100

    final_total = total - discount_amount

    return final_total


# Customer 1
cart1 = create_cart("Aarav", 10)

add_to_cart(cart1, "Laptop", 50000, 1)
add_to_cart(cart1, "Mouse", 500, 2)


# Customer 2
cart2 = create_cart("Riya", 5)

add_to_cart(cart2, "Phone", 20000, 1)


# Printing carts
print("\nCart 1")
print(cart1)

print("\nCart 2")
print(cart2)


# Printing totals
print("\nCart 1 Total:", calculate_total(cart1))
print("Cart 2 Total:", calculate_total(cart2))


# Tuple Example
price_tuple = (100, 200, 300)

# This will raise TypeError
# update_price(price_tuple, 500)


# Discussion Answers

# discount=0 is safe because int is immutable.
# cart=[] is dangerous because list is mutable.

# Rebinding means assigning a new value.
# Mutating means changing the existing object.

# Mutable: list, dict, set
# Immutable: tuple, str, int

# Changes in list reflect outside the function
# because lists are mutable.
# This will raise TypeError
# update_price(price_tuple, 500)