# Using dictionaries to store product Prices

product_price = {'Apple': 0.67, 'milk': 1.49, 'Avocado': 1.49}

print(product_price)
print(product_price['Avocado'])

# Let's implement a simple voting system
voted = {}


def check_voted(name):
    if voted.get(name):
        print(f'Kick {name} Out!!!')
    else:
        voted[name] = True
        print(f'Let {name} Vote')


check_voted('Sam')
check_voted('Paul')
check_voted('Sam')
