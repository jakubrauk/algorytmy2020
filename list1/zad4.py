import numpy as np

def productExits(receipts, products):
	for order in receipts:
		products_exits = False
		for product in products:
			if order[2] == product[0]:
				products_exits = True
		if not products_exits:
			print(f'Produkt id: {order[2]}, nie istnieje')		

def totalCost(receipts):
	for order in receipts:
		customer_id = order[1]
		final_cost = products[order[2]][1] * order[3]
		print(f'Klient id: {customer_id}, zapłacił: {final_cost}zł')

receipts = np.array([(1, 1, 1, 4), (2, 2, 1, 3), (3, 3, 2, 2.5)],
	dtype=[('receipt_id', '<i4'), ('customer_id', '<i4'), ('product_id', '<i4'), ('product_quant', '<f4')])

products = np.array([(1, 2.5, 'pieces'), (2, 5, 'kg')],
	dtype=[('product_id', '<i4'), ('price', '<f4'), ('piece_or_kg', '<U32')])

productExits(receipts, products)
totalCost(receipts)