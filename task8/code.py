def process_canteen_orders(menu_stock, prices, orders):
    stock = menu_stock.copy()
    total_sales = 0.0
    processed_orders = []
    
    for order_id, order_items in enumerate(orders):
        bill = 0.0
        accepted_items = []
        rejected_items = []
        
        for item, qty in order_items.items():
            if item in stock and stock[item] >= qty:
                stock[item] -= qty
                bill += qty * prices[item]
                accepted_items.append((item, qty))
            else:
                available = stock.get(item, 0)
                rejected_items.append((item, qty, available))
                if available > 0:
                    stock[item] = 0
                    bill += available * prices[item]
                    accepted_items.append((item, available))
                    
        total_sales += bill
        processed_orders.append((order_id + 1, accepted_items, rejected_items, round(bill, 2)))
        
    return total_sales, stock, processed_orders

menu_stock = {"Burger": 10, "Pizza": 5, "Soda": 20}
prices = {"Burger": 5.50, "Pizza": 12.00, "Soda": 2.00}

orders = [
    {"Burger": 3, "Soda": 5},
    {"Pizza": 6, "Soda": 10},
    {"Burger": 8, "Pizza": 2}
]

sales, remaining_stock, order_summary = process_canteen_orders(menu_stock, prices, orders)

print("Total Sales Revenue:", sales)
print("Remaining Stock:", remaining_stock)
print("Order Summary:", order_summary)

