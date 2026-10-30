import re

def analyze_registrations(records):
    valid_records = []
    duplicate_records = []
    error_report = {
        "Field Count Error": [],
        "Format Error": [],
        "Length Error": []
    }
    seen_ids = set()
    
    email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    id_regex = r"^REG\d{3}$"
    
    for record in records:
        parts = record.split(",")
        parts = [p.strip() for p in parts]
        
        if len(parts) != 4:
            error_report["Field Count Error"].append(record)
            continue
            
        reg_id, name, email, date_str = parts
        
        if not re.match(id_regex, reg_id) or len(reg_id) != 6:
            error_report["Length Error" if len(reg_id) != 6 else "Format Error"].append((record, "Invalid ID"))
            continue
            
        if not re.match(email_regex, email):
            error_report["Format Error"].append((record, "Invalid Email"))
            continue
            
        if reg_id in seen_ids:
            duplicate_records.append(record)
        else:
            seen_ids.add(reg_id)
            valid_records.append((reg_id, name, email, date_str))
            
    return valid_records, duplicate_records, error_report

raw_records = [
    "REG001, Alice Smith, alice@example.com, 2026-03-01",
    "REG002, Bob Jones, bob.jones@domain.org, 2026-03-02",
    "REG001, Alice Duplicate, alice.dup@example.com, 2026-03-03",
    "REGX99, Charlie, charlie@example.com, 2026-03-04",
    "REG003, Diana, invalid-email, 2026-03-05",
    "REG004, Extra, field, data, 2026-03-06"
]

valid, duplicates, errors = analyze_registrations(raw_records)

print("Valid Records:", valid)
print("Duplicate Records:", duplicates)
print("Error Report:", errors)

