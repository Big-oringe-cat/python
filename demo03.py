def discount(price,rate):
    final_price=price*rate
    return final_price
old_price=float(input('please insert the price:'))
rate=float(input('please insert rate:'))
new_price=discount(price=old_price,rate=rate)
print('now,price is ',new_price)
print(final_price)
