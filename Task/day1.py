# Input student details
sname = input("Enter the name of the student : ")
math = int(input("Enter your mark in Maths : "))
sci = int(input("Enter your mark in Science : "))
eng = int(input("Enter your mark in English : "))

# Validate marks
if math < 0 or math > 100 or sci < 0 or sci > 100 or eng < 0 or eng > 100:
    print("Invalid mark entered")
else:
    # Calculate total, average, and percentage
    totalm = math + sci + eng
    avg = totalm / 3
    percent = (totalm / 300) * 100
    
    # Display results
    print(f"\nStudent Name: {sname}")
    print(f"Total = {totalm}")
    print(f"Average = {avg:.2f}")
    print(f"Percentage = {percent:.2f}%")
    
    # Determine grade
    if percent >= 90:
        grade = "A Grade"
    elif percent >= 80:
        grade = "B Grade"
    elif percent >= 70:
        grade = "C Grade"
    elif percent >= 60:
        grade = "D Grade"
    else:
        grade = "Fail"
    
    print(f"Grade: {grade}")
    
    # Display subject-wise marks
    print("\nSubject-wise Marks:")
    subjects = ["Maths", "Science", "English"]
    marks = [math, sci, eng]
    
    for i in range(len(subjects)):
        print(f"{subjects[i]}: {marks[i]}")
    
    # Display as list 
    combine = list(zip(subjects, marks))
    print(combine))
