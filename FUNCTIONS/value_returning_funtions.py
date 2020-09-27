DSICOUNT_PERCENTAGE = 0.20
def main():
    reg_price = get_regular_price()
    sale_price =  discount(reg_price)
    print('The sale price is $ ',format(sale_price,',.2f'),sep='')

def get_regular_price():
    price = float(input("Enter the item's regular price: "))
    return price

def discount(reg_price):
    i = reg_price * DSICOUNT_PERCENTAGE
    return i

main()
