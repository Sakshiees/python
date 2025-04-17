def calculate_marks():
    # Define the subjects
    subjects = [
        "Microcontroller",
        "Data Structure",
        "Professional Ethics",
        "Environmental Studies",
        "Computer Networks",
        "Information System Management"
    ]
    
    marks = {}
    
    print("Enter marks for each subject (out of 100):")
    print("----------------------------------------")
    
    # Get marks for each subject
    for subject in subjects:
        while True:
            try:
                mark = float(input(f"{subject}: "))
                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break
                else:
                    print("Marks must be between 0 and 100. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    # Calculate total and average
    total = sum(marks.values())
    average = total / len(subjects)
    
    # Determine grade
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    elif average >= 50:
        grade = 'E'
    else:
        grade = 'F'
    
    # Display results
    print("\n=== Results ===")
    print("Subject-wise Marks:")
    for subject, mark in marks.items():
        print(f"{subject}: {mark}")
    
    print("\nSummary:")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average:.2f}")
    print(f"Grade: {grade}")

# Run the program
calculate_marks()
