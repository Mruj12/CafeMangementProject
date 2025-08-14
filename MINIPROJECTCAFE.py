menu={
    "pizza":120,
    "pasta":100,
    "burger":80,
    "cold coffee":70,
    "sandwich":80,
    "maggie":50
}
print("Welcome to Hunger Monkey Cafe!")
print("pizza: Rs120\n pasta: Rs100\n burger: Rs80\n cold coffee: Rs70\n sandwich: Rs80\n maggie: Rs50\n")

order_total=0

item_1=input("what would you like to order?")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your {item_1} added to cart")
else:
    print(f"{item_1} is currently not avaible")

another_other=input("would you prefer anything else?(Yes/No)")
if another_other == "Yes":
    item_2=input("what you would like to order?")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"your{item_2}added to cart")
    else:
        print(f"{item_2}currently not available!")
print(f"Your Total Bill={order_total}")

