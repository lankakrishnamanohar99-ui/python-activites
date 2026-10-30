def analyze_orders(product_names, initial_orders, dispatched, returned):
    processed_results = []
    inconsistent_records = []
    
    for i in range(len(product_names)):
        name = product_names[i]
        ordered = initial_orders[i]
        disp = dispatched[i]
        ret = returned[i]
        
        if disp > ordered:
            inconsistent_records.append((name, "Dispatched exceeds Initial Order"))
            continue
            
        if ret > disp:
            inconsistent_records.append((name, "Returned exceeds Dispatched Quantity"))
            continue
            
        outstanding = ordered - disp
        net_inventory_change = disp - ret
        
        processed_results.append((name, outstanding, net_inventory_change))
        
    return processed_results, inconsistent_records

product_names = ["Item_A", "Item_B", "Item_C"]
initial_orders = [100, 200, 150]
dispatched = [90, 210, 150]
returned = [5, 10, 20]

results, inconsistencies = analyze_orders(product_names, initial_orders, dispatched, returned)

print("Processed Results (Product, Outstanding, Net Dispatched):", results)
print("Inconsistent Records:", inconsistencies)

