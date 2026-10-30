def analyze_hospital_resources(wards, occupancy_data, staff_data, equipment_data, thresholds):
    report = []
    
    for i in range(len(wards)):
        ward_name = wards[i]
        beds_occ, max_beds = occupancy_data[i]
        staff_avail, min_staff = staff_data[i]
        equip_avail, min_equip = equipment_data[i]
        
        shortages = []
        
        if beds_occ > max_beds:
            shortages.append("Bed Overflow")
        if staff_avail < min_staff:
            shortages.append("Staff Shortage")
        if equip_avail < min_equip:
            shortages.append("Equipment Shortage")
            
        if len(shortages) >= 2:
            priority = "Critical"
        elif len(shortages) == 1:
            priority = "Moderate"
        else:
            priority = "Normal"
            
        report.append((ward_name, priority, shortages))
        
    return report

wards = ["ICU", "Emergency", "General Ward"]
occupancy_data = [(15, 12), (30, 30), (40, 50)]
staff_data = [(8, 10), (12, 10), (15, 20)]
equipment_data = [(5, 6), (8, 8), (10, 10)]

thresholds = {}

results = analyze_hospital_resources(wards, occupancy_data, staff_data, equipment_data, thresholds)

print("Hospital Resource Allocation Report:", results)

