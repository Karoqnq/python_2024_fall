female_students = int(input("Enter the number of female students: "))
male_students = int(input("Enter the number of male students: "))

if female_students == 0 and male_students == 0:
    print()
    print("Female: 0.0 %")
    print("Male: 0.0 %")
    
else:
    total_students = female_students + male_students
    female_percentage = (female_students / total_students) * 100
    male_percentage = (male_students / total_students) * 100

    print()
    print(f"Female: {female_percentage:.1f} %")
    print(f"Male: {male_percentage:.1f} %")