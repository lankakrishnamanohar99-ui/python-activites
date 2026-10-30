def audit_eligibility(students):
    eligible_students = []
    ineligible_report = {
        "Fee Due": [],
        "Low Attendance": [],
        "Low Internal Marks": [],
        "Multiple Issues": []
    }
    
    for student in students:
        sid, name, fee_paid, total_fee, attendance, marks = student
        issues = []
        
        if fee_paid < total_fee:
            issues.append("Fee Due")
        if attendance < 75.0:
            issues.append("Low Attendance")
        if marks < 40.0:
            issues.append("Low Internal Marks")
            
        if not issues:
            eligible_students.append((sid, name))
        else:
            if len(issues) > 1:
                ineligible_report["Multiple Issues"].append((sid, name, issues))
            else:
                ineligible_report[issues[0]].append((sid, name))
                
    return eligible_students, ineligible_report

students = [
    (101, "Alice", 5000, 5000, 85.5, 65.0),
    (102, "Bob", 3000, 5000, 78.0, 50.0),
    (103, "Charlie", 5000, 5000, 60.0, 35.0),
    (104, "Diana", 2000, 5000, 65.0, 30.0),
    (105, "Ethan", 5000, 5000, 92.0, 85.0)
]

eligible, report = audit_eligibility(students)

print("Eligible Students:", eligible)
print("Ineligible Report by Reason:", report)

