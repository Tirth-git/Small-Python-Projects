menu={"pizza": 220,
      "nachos": 119,
      "popcorn": 205,
      "fries": 105,
      "chips": 60,
      "samosa": 78,
      "pretzel": 91,
      "coco-cola": 50}

cart=[]
total=0

print("--------------MENU--------------")
for key,value in menu.items():
    print(f"{key:15}: ₹{value}")
print("--------------------------------")

while True:
    food=input("Select An Item to Purchase (Press q to Quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("----------YOUR ORDER------------")
for food in cart:
    total+= menu.get(food)
    print(food, end=" ")
print()
print(f"Your Total is:- ₹{total}")