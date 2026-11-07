"""
Class Marks Analyzer
--------------------
Collects names and marks for a whole class, then shows statistics:
average, highest, lowest, pass/fail counts, above-average students
and a ranked list from highest to lowest marks.
"""

PASS_MARK = 50  # 50 or above = Pass


# ---------- Input functions ----------
def get_student_count():
    # Keep asking until the user enters a whole number greater than 0.
    while True:
        entry = input("How many students are in the class? ").strip()
        if entry.isdigit() and int(entry) > 0:
            return int(entry)
        print("  Invalid input! Please enter a number greater than 0.")


def get_student_name(position):
    # Keep asking until the user types a non-empty name; return it cleaned.
    while True:
        name = input(f"Enter name of student {position}: ").strip().title()
        if name != "":
            return name
        print("  Name cannot be empty.")


def get_valid_marks(name):
    # Keep asking until marks are a whole number between 0 and 100.
    while True:
        entry = input(f"Enter marks for {name} (0-100): ").strip()
        if entry.isdigit() and 0 <= int(entry) <= 100:
            return int(entry)
        print("  Invalid marks! Enter a whole number from 0 to 100.")


# ---------- Analysis functions ----------
def find_students_with_marks(names, marks, target):
    # Return a list of ALL students whose marks equal the target (handles ties).
    matched = []
    for i in range(len(marks)):
        if marks[i] == target:
            matched.append(names[i])
    return matched


def count_pass_fail(marks):
    # Return (passing_count, failing_count) based on PASS_MARK.
    passed = 0
    for mark in marks:
        if mark >= PASS_MARK:
            passed += 1
    failed = len(marks) - passed
    return passed, failed


def find_above_average(names, marks, average):
    # Return a list of (name, marks) for students scoring above the average.
    result = []
    for i in range(len(marks)):
        if marks[i] > average:
            result.append((names[i], marks[i]))
    return result


# ---------- Main program ----------
def main():
    print("--- Class Marks Analyzer ---\n")

    student_names = []
    student_marks = []

    # 1. Collect data: two parallel lists (same index = same student)
    total_students = get_student_count()
    for number in range(1, total_students + 1):
        name = get_student_name(number)
        marks = get_valid_marks(name)
        student_names.append(name)    # store name
        student_marks.append(marks)   # store marks at the same position

    # 2. Calculations
    average = sum(student_marks) / len(student_marks)
    highest = max(student_marks)
    lowest = min(student_marks)
    toppers = find_students_with_marks(student_names, student_marks, highest)
    lowest_scorers = find_students_with_marks(student_names, student_marks, lowest)
    passed, failed = count_pass_fail(student_marks)
    above_average = find_above_average(student_names, student_marks, average)

    # 3. Display report
    line = "=" * 42
    print("\n" + line)
    print(f"{'CLASS PERFORMANCE REPORT':^42}")
    print(line)
    print(f"Total students : {len(student_marks)}")
    print(f"Class average  : {average:.2f}")
    print(f"Highest marks  : {highest}  ({', '.join(toppers)})")
    print(f"Lowest marks   : {lowest}  ({', '.join(lowest_scorers)})")
    print(f"Passing (>= {PASS_MARK}): {passed}")
    print(f"Failing (< {PASS_MARK}) : {failed}")

    print("\nStudents above class average:")
    if above_average:
        for name, marks in above_average:
            print(f"  - {name}: {marks}")
    else:
        print("  None (everyone scored the same).")

    # Pair each mark with its name, then sort. reverse=True = highest first.
    ranking = sorted(zip(student_marks, student_names), reverse=True)
    print("\nRanking (highest to lowest):")
    print(f"  {'Rank':<6}{'Name':<20}{'Marks':>6}")
    for rank, (marks, name) in enumerate(ranking, start=1):
        print(f"  {rank:<6}{name:<20}{marks:>6}")
    print(line)


# Runs main() only when this file is executed directly
if __name__ == "__main__":
    main()
