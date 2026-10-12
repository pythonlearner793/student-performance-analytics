# functions.py

def assign_grade(average_marks):
    """Assigns grades based on a clearly defined grading rule."""
    if average_marks >= 85:
        return 'A'
    elif average_marks >= 70:
        return 'B'
    elif average_marks >= 50:
        return 'C'
    else:
        return 'D (Fail)'

def check_pass_fail(average_marks, attendance):
    """Identifies pass/fail students using clearly defined conditions."""
    if average_marks >= 50 and attendance >= 70:
        return 'Pass'
    else:
        return 'Fail'
