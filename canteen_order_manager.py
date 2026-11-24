#Johann Dominic Jimenez
#8 - Sampaguita
def update(food):
    print(f"Updated Order: {food}")
food = []
for i in range(1, 6):
    order = str(input(f"Enter order {i}: "))
    food.append(order)
print(f"Original orders: {food}")
add = input("Enter additional order: ")
food.append(add)
update(food)
priority = input("Enter priority: ")
food.insert(0, priority)
update(food)
search = input(f"Search for an order:")
occurence = food.count(search)
if occurence == 0:
    print(f"Sorry, no order with that search was found")
else:
    print(f"Number of occurences: {occurence}")
    index = food.index(search)
    print(f"First index: {index}")
cancel = input("Enter order to cancel: ")
food.remove(cancel)
update(food)

print(f"Removed order: {food[5]}")
food.pop(5)
print(f"FINAL ORDER REPORT")
print(f"Orders: {food}")
print(f"Number of orders: {len(food)}")
