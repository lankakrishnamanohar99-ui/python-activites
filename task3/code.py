def quality_control_audit(production_data, threshold):
    audit_results = []
    flagged_batches = []
    
    for prod_idx, batches in enumerate(production_data):
        product_results = []
        for batch_idx, (prod_qty, def_qty) in enumerate(batches):
            defect_pct = (def_qty / prod_qty) * 100 if prod_qty > 0 else 0.0
            status = "FAIL" if defect_pct > threshold else "PASS"
            product_results.append((batch_idx, prod_qty, def_qty, round(defect_pct, 2), status))
            if status == "FAIL":
                flagged_batches.append((prod_idx, batch_idx, round(defect_pct, 2)))
        audit_results.append(product_results)
        
    return audit_results, flagged_batches

threshold = 5.0
production_data = [
    [(1000, 20), (500, 35), (800, 10)],
    [(1200, 70), (600, 12)]
]

results, flagged = quality_control_audit(production_data, threshold)

print("Audit Results Matrix:", results)
print("Flagged Batches Exceeding Threshold:", flagged)

