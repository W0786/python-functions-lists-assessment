"""
Student Result Card Generator
-----------------------------
Takes a student's details and marks in five subjects,
then prints a neatly formatted result card.
"""

# ---------- Constants (values that never change) ----------
SUBJECTS = ["English", "Urdu", "Mathematics", "Science", "Computer"]
MAX_MARKS_PER_SUBJECT = 100
SUBJECT_PASS_MARK = 40  # Below this in ANY subject = Fail


# ---------- Functions ----------
def format_name(name):
    """Remove extra spaces and capitalize each word.
    Example: '   ali raza  ' -> 'Ali Raza'
    """
    return name.strip().title()


def get_valid_roll_number():
    """Keep asking until the roll number contains digits only."""
    while True:
        roll_no = input("Enter roll number: ").strip()
        if roll_no.isdigit():
            return roll_no
        print("  Invalid roll number! Please use digits only (0-9).")


def get_valid_marks(subject):
    """Keep asking until the user enters a whole number between 0 and 100."""
    while True:
        entry = input(f"Enter marks for {subject} (0-100): ").strip()

        # Step 1: is it a number at all?
        if not entry.isdigit():
            print("  Invalid input! Please enter a whole number.")
            continue

        # Step 2: is it in the allowed range?
        marks = int(entry)
        if 0 <= marks <= MAX_MARKS_PER_SUBJECT:
            return marks
        print("  Marks must be between 0 and 100.")


def calculate_percentage(total, max_total):
    """Return percentage = (obtained / maximum) * 100."""
    return (total / max_total) * 100


def get_grade(percentage):
    """Return the letter grade for a given percentage."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"


def get_status(marks_list, grade):
    """Return 'Pass' or 'Fail'.
    Fail if the grade is Fail OR any single subject is below 40.
    """
    if grade == "Fail" or min(marks_list) < SUBJECT_PASS_MARK:
        return "Fail"
    return "Pass"


def print_result_card(name, roll_no, marks_list, total, max_total,
                      percentage, grade, status):
    """Display the result card using f-strings."""
    line = "=" * 40
    thin = "-" * 40

    print("\n" + line)
    print(f"{'STUDENT RESULT CARD':^40}")  # ^40 = center in 40 characters
    print(line)
    print(f"Name        : {name}")
    print(f"Roll Number : {roll_no}")
    print(thin)
    print(f"{'Subject':<20}{'Marks':>10}")
    print(thin)

    for subject, marks in zip(SUBJECTS, marks_list):
        print(f"{subject:<20}{marks:>10}")

    print(thin)
    print(f"{'Total':<20}{f'{total}/{max_total}':>10}")
    print(f"{'Percentage':<20}{f'{percentage:.2f}%':>10}")
    print(f"{'Grade':<20}{grade:>10}")
    print(f"{'Final Status':<20}{status:>10}")

    # Explain WHY the student failed (if due to a low subject mark)
    failed_subjects = [s for s, m in zip(SUBJECTS, marks_list)
                       if m < SUBJECT_PASS_MARK]
    if failed_subjects:
        print(thin)
        print(f"Remark: Below {SUBJECT_PASS_MARK} in {', '.join(failed_subjects)}")
    print(line)


# ---------- Main program ----------
def main():
    print("--- Student Result Card Generator ---\n")

    # 1. Collect student details
    name = format_name(input("Enter student name: "))
    roll_no = get_valid_roll_number()

    # 2. Collect and validate marks for every subject
    marks_list = []
    for subject in SUBJECTS:
        marks_list.append(get_valid_marks(subject))

    # 3. Calculations
    total = sum(marks_list)
    max_total = len(SUBJECTS) * MAX_MARKS_PER_SUBJECT
    percentage = calculate_percentage(total, max_total)
    grade = get_grade(percentage)
    status = get_status(marks_list, grade)

    # 4. Show the result card
    print_result_card(name, roll_no, marks_list, total, max_total,
                      percentage, grade, status)


# Runs main() only when this file is executed directly
if __name__ == "__main__":
    main()
