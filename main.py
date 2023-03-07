from shop.model import Product, Category

phone = Category('Phones')

iphone15 = Product('Iphone 15 black', 'Apple', 'Iphone 15', 990, 'black', 256, category=phone)
Samsung = Product('Samsung S23', 'Samsung', 'S23', 850, 'white', 512, category=phone)

print(iphone15.__dict__)
print(iphone15.__dict__)