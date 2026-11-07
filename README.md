# Python Functions & Lists Assessment

## 1. Project Overview

This repository contains two separate Python programs that practise **functions**, **string manipulation**, **lists** and **loops**. Both programs run in the terminal, validate every user input, and use clear function names with short comments so that beginners can follow the logic easily.

```text
python-functions-lists-assessment/
├── result_card_generator.py
├── class_marks_analyzer.py
└── README.md
```

| Task | File | Main Topics |
|---|---|---|
| Task 1: Student Result Card Generator | `result_card_generator.py` | Functions (`def`, parameters, `return`) and string manipulation |
| Task 2: Class Marks Analyzer | `class_marks_analyzer.py` | Lists (`append()`, `len()`, `sum()`, `max()`, `min()`, `sorted()`) and loops |

---

## 2. Description of the Programs

### Task 1: Student Result Card Generator (`result_card_generator.py`)

Generates a formatted result card for **one student**.

**Requirements covered**

- Asks for the student's name, roll number and marks in five subjects.
- Uses the required functions: `get_valid_marks(subject)`, `calculate_percentage(total, max_total)`, `get_grade(percentage)` and `format_name(name)`.
- Validates input: marks must be between 0 and 100, and the roll number must contain digits only (checked with `.isdigit()`).
- Cleans the student's name using `.strip()` and `.title()`.
- Applies the grading criteria shown below.
- Generates the result card using Python f-strings, showing: name, roll number, marks in all five subjects, total marks, percentage (2 decimal places), letter grade and final status (Pass/Fail).

**Grading criteria**

| Percentage | Grade |
|---|---|
| 90 and above | A+ |
| 80 - 89 | A |
| 70 - 79 | B |
| 60 - 69 | C |
| 50 - 59 | D |
| Below 50 | Fail |

> **Important rule:** if any subject mark is below 40, the final result is **Fail**, regardless of the overall percentage.

### Task 2: Class Marks Analyzer (`class_marks_analyzer.py`)

Analyzes the academic performance of an **entire class**.

**Requirements covered**

- Asks how many students are in the class.
- Maintains two separate lists: `student_names = []` and `student_marks = []`.
- Uses `.append()` to store names and marks.
- Validates every mark (0 - 100) and asks again if the input is invalid.
- Calculates and displays the class average, the highest marks with the student(s) who achieved them, and the lowest marks with the student(s) who achieved them.
- Counts passing students (50 or above) and failing students (below 50).
- Displays all students who scored above the class average.
- Displays student marks sorted from highest to lowest.
- Implements several parts of the program with custom functions (more than the required two).

---

## 3. Python Concepts and Functions Used

### Task 1

| Concept | Where it is used |
|---|---|
| Custom functions (`def`, parameters, `return`) | `get_valid_marks()`, `calculate_percentage()`, `get_grade()`, `format_name()`, `get_valid_roll_number()`, `get_status()`, `print_result_card()` |
| String methods | `.strip()`, `.title()`, `.isdigit()`, `.join()` |
| f-strings | Result card formatting with alignment (`<`, `>`, `^`) and `.2f` for 2 decimal places |
| Loops | `while True` for input validation, `for` to print each subject |
| Conditions | `if / elif / else` for grading and pass/fail logic |
| Built-in functions | `sum()`, `min()`, `zip()`, `len()` |

### Task 2

| Concept | Where it is used |
|---|---|
| Lists | `student_names`, `student_marks` |
| List method | `.append()` |
| Built-in functions | `len()`, `sum()`, `max()`, `min()`, `sorted()`, `zip()`, `enumerate()` |
| Custom functions | `get_student_count()`, `get_student_name()`, `get_valid_marks()`, `find_students_with_marks()`, `count_pass_fail()`, `find_above_average()` |
| Loops | `for` loops over indexes and lists, `while True` for validation |
| Input validation | `.isdigit()` plus range checks |

### General Practices Followed

- Every function has a clear name and a short comment or docstring explaining its purpose.
- All user input is validated and invalid values are handled without crashing.
- Meaningful variable and function names are used.
- Proper indentation and formatting, with comments explaining the important logic.
- Both programs were tested with multiple input scenarios (see Section 6).

---

## 4. How to Run

**Requirements:** Python 3.8 or newer. No external libraries are needed.

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/python-functions-lists-assessment.git
cd python-functions-lists-assessment

# 2. Run Task 1
python result_card_generator.py

# 3. Run Task 2
python class_marks_analyzer.py
```

On some systems you may need to use `python3` instead of `python`.

---

## 5. Sample Input and Output

### Task 1: Result Card Generator

**Input**

```text
Enter student name: sara khan
Enter roll number: 1024
Enter marks for English (0-100): 95
Enter marks for Urdu (0-100): 88
Enter marks for Mathematics (0-100): 92
Enter marks for Science (0-100): 85
Enter marks for Computer (0-100): 90
```

**Output**

```text
========================================
          STUDENT RESULT CARD           
========================================
Name        : Sara Khan
Roll Number : 1024
----------------------------------------
Subject                  Marks
----------------------------------------
English                     95
Urdu                        88
Mathematics                 92
Science                     85
Computer                    90
----------------------------------------
Total                  450/500
Percentage              90.00%
Grade                       A+
Final Status              Pass
========================================
```

**Example with a subject below 40** (Science = 35, other marks: 85, 92, 78, 88)

```text
----------------------------------------
Total                  378/500
Percentage              75.60%
Grade                        B
Final Status              Fail
----------------------------------------
Remark: Below 40 in Science
========================================
```

### Task 2: Class Marks Analyzer

**Input**

```text
How many students are in the class? 5
Enter name of student 1: ali
Enter marks for Ali (0-100): 80
Enter name of student 2: sara
Enter marks for Sara (0-100): 90
Enter name of student 3: bilal
Enter marks for Bilal (0-100): 90
Enter name of student 4: hina
Enter marks for Hina (0-100): 35
Enter name of student 5: zain
Enter marks for Zain (0-100): 35
```

**Output**

```text
==========================================
         CLASS PERFORMANCE REPORT         
==========================================
Total students : 5
Class average  : 66.00
Highest marks  : 90  (Sara, Bilal)
Lowest marks   : 35  (Hina, Zain)
Passing (>= 50): 3
Failing (< 50) : 2

Students above class average:
  - Ali: 80
  - Sara: 90
  - Bilal: 90

Ranking (highest to lowest):
  Rank  Name                 Marks
  1     Sara                    90
  2     Bilal                   90
  3     Ali                     80
  4     Zain                    35
  5     Hina                    35
==========================================
```

---

## 6. Testing Scenarios

Both programs were tested with the following cases:

| Scenario | Program | Result |
|---|---|---|
| Name with extra spaces and lowercase (`"   ali raza  "`) | Task 1 | Cleaned to `Ali Raza` |
| Roll number with letters (`abc`) | Task 1 | Rejected, asks again |
| Marks above 100 (`150`) or text (`xyz`) | Both | Rejected, asks again |
| One subject below 40 with a high percentage | Task 1 | Final status is Fail with a remark |
| Student count of `0` or text | Task 2 | Rejected, asks again |
| Empty student name | Task 2 | Rejected, asks again |
| Two students with the same highest/lowest marks | Task 2 | Both names are shown |
| All students with equal marks | Task 2 | "None" shown for above-average list, no crash |

---

## Author

Your Name
