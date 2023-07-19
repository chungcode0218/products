products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')

	p = []             # p 為大清單(products)中的小清單	
	p.append(name)
	p.append(price)    # 此三行可寫成 p = [name, price]
	
	products.append(p)

print(products)

products[0][0]