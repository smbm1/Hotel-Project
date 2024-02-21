menu = ['tea', 'coffee', 'burger', 'roll']
stock = [40, 40, 15, 20]
price = [1.9, 2.1, 3.5, 2.7]

menu_stock = list(zip(menu,stock))
menu_price = list(zip(menu,price))

sd = dict(menu_stock)
pd = dict(menu_price)


total_val = 0 
for item in sd.keys() and pd.keys():
    stock = sd[item]
    price = pd[item]
    item_value = stock*price
    total_val += item_value


print(f"the total item value is £{total_val:.2f}")