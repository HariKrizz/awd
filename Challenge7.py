
prdct_price = {'Laptop' : '₹ 61,999', 'Headset' : '₹ 3499', 'Mouse' : '₹ 999', 'Modem' : '₹ 2999' }

print('Available products in Stock')
print('---------------------------')
print(prdct_price.keys())

prdct = input("Enter product name to check Price: ")
if prdct in prdct_price.keys():
    print('The Price of ' +prdct+ ' is:',prdct_price.get(prdct))
else:
    print("Currently out of stock, arriving soon!")
