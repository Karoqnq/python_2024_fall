def grade_exam(applicant_list, passing_score):
    # In the list applicant names and exam scores are in tuples
    # Should return a new list of tuples which contains those applicants who passed the exam
    # List Comprehension > Create a new variable which makes a new list of tuples based on the exam score of the applicant
    passed_applicant = [(applicant_name, exam_score) for applicant_name, exam_score in applicant_list if exam_score >= passing_score ]
    
    return passed_applicant

def main():
    applicants = [("Ann", 30), ("Jack", 25), ("Jill", 40)]
    passed_applicants = grade_exam(applicants, 30)

    print("Entry exam passed")

    for name, points in passed_applicants:
        print(f"{name}, {points} points")

if __name__ == "__main__":
    main()