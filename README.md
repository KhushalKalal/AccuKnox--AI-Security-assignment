# AI Security Engineer Trainee – Assignment 1

## Included
- Q1: REST API → SQLite → display books
- Q2: API → calculate average → bar chart
- Q3: CSV → SQLite

## Requirements
Python 3.7+ and internet access.

Install dependencies:
```bash
pip install -r assignment1/requirements.txt
```

## Run
From the `assignment1` folder:
```bash
python q1_api_sqlite.py
python q2_student_scores.py
python q3_csv_sqlite.py
```

Q1 creates `books.db` and Q2 creates `student_scores.png`. Q3 creates `users.db`.

## Q2 assumption
The selected demo API (`dummyjson.com/users`) provides user data, not student test scores. For demonstration, a deterministic score is derived from age. This assumption should be documented in the submission. A real student-score API/dataset can replace this source later without changing the overall processing/visualization flow.
