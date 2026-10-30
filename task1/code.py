def reconcile_inventory(inventory, targets, warehouses, products):
    num_warehouses = len(inventory)
    num_products = len(inventory[0])
    
    diffs = [[inventory[w][p] - targets[w][p] for p in range(num_products)] for w in range(num_warehouses)]
    
    shortages = []
    surpluses = []
    
    for w in range(num_warehouses):
        for p in range(num_products):
            d = diffs[w][p]
            if d < 0:
                shortages.append((w, p, -d))
            elif d > 0:
                surpluses.append((w, p, d))
                
    transfers = []
    s_idx = 0
    t_idx = 0
    
    while s_idx < len(surpluses) and t_idx < len(shortages):
        s_warehouse, s_product, s_qty = surpluses[s_idx]
        t_warehouse, t_product, t_qty = shortages[t_idx]
        
        if s_product == t_product:
            transfer_qty = min(s_qty, t_qty)
            transfers.append((warehouses[s_warehouse], warehouses[t_warehouse], products[s_product], transfer_qty))
            
            if s_qty > t_qty:
                surpluses[s_idx] = (s_warehouse, s_product, s_qty - transfer_qty)
                t_idx += 1
            elif s_qty < t_qty:
                shortages[t_idx] = (t_warehouse, t_product, t_qty - transfer_qty)
                s_idx += 1
            else:
                s_idx += 1
                t_idx += 1
        else:
            t_idx += 1
            
    return diffs, shortages, surpluses, transfers

warehouses = ["Warehouse_A", "Warehouse_B"]
products = ["Product_1", "Product_2"]

inventory = [
    [10, 20],
    [30, 5]
]

targets = [
    [15, 10],
    [20, 15]
]

diffs, shortages, surpluses, transfers = reconcile_inventory(inventory, targets, warehouses, products)

print("Differences Matrix:", diffs)
print("Shortages:", shortages)
print("Surpluses:", surpluses)
print("Required Transfers:", transfers)

