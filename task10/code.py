def allocate_hostel_rooms(rooms, students):
    room_capacities = {room: cap for room, cap in rooms.items()}
    allocations = {room: [] for room in rooms}
    seen_students = set()
    duplicates = []
    unallocated = []
    
    for student_id, name, gender, preferred_room in students:
        if student_id in seen_students:
            duplicates.append((student_id, name))
            continue
            
        seen_students.add(student_id)
        
        if preferred_room in room_capacities and room_capacities[preferred_room] > 0:
            allocations[preferred_room].append((student_id, name, gender))
            room_capacities[preferred_room] -= 1
        else:
            allocated = False
            for room in room_capacities:
                if room_capacities[room] > 0:
                    allocations[room].append((student_id, name, gender))
                    room_capacities[room] -= 1
                    allocated = True
                    break
            if not allocated:
                unallocated.append((student_id, name, gender))
                
    return allocations, duplicates, unallocated, room_capacities

rooms = {"BlockA-101": 2, "BlockB-201": 1}
students = [
    (101, "Alice", "F", "BlockA-101"),
    (102, "Bob", "M", "BlockB-201"),
    (101, "Alice Duplicate", "F", "BlockA-101"),
    (103, "Charlie", "M", "BlockA-101"),
    (104, "Diana", "F", "BlockB-201")
]

allocations, duplicates, unallocated, remaining_caps = allocate_hostel_rooms(rooms, students)

print("Room Allocations:", allocations)
print("Duplicate Assignments Detected:", duplicates)
print("Unallocated Demand:", unallocated)
print("Remaining Capacities:", remaining_caps)

