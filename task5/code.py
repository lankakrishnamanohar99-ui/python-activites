def analyze_exam_performance(answer_key, student_responses):
    num_questions = len(answer_key)
    num_students = len(student_responses)
    correct_counts = [0] * num_questions
    
    for response in student_responses:
        for q_idx in range(num_questions):
            if q_idx < len(response) and response[q_idx] == answer_key[q_idx]:
                correct_counts[q_idx] += 1
                
    success_rates = []
    classifications = []
    
    for q_idx in range(num_questions):
        rate = (correct_counts[q_idx] / num_students) * 100
        success_rates.append(round(rate, 2))
        
        if rate < 50.0:
            classification = "Difficult"
        elif rate <= 80.0:
            classification = "Moderate"
        else:
            classification = "Easy"
            
        classifications.append((q_idx + 1, round(rate, 2), classification))
        
    missed_questions = sorted(classifications, key=lambda x: x[1])
    
    return success_rates, classifications, missed_questions

answer_key = "ABCAD"
student_responses = [
    "ABCAD",
    "ABCCD",
    "ABCAA",
    "BBCAD",
    "ABBAD"
]

rates, classifications, missed = analyze_exam_performance(answer_key, student_responses)

print("Success Rates (%):", rates)
print("Question Classifications:", classifications)
print("Ranked by Missed Frequency:", missed)

