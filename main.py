# main.py
import pandas as pd
import numpy as np
from functions import assign_grade, check_pass_fail

def main():
    # Step 2: Read the Data
    # Load and organize the data using Pandas DataFrame
    try:
        df = pd.read_csv('students.csv')
    except FileNotFoundError:
        print("Error: students.csv not found.")
        return

    print("--- Student Performance Analytics System ---")
    print(f"Total student records loaded: {len(df)}\n")

    # Step 3: Process the Data
    # Use NumPy for numerical calculations (totals and averages)
    subjects = ['Math_Marks', 'Science_Marks', 'English_Marks']
    
    # Calculate total marks and average marks for each student
    df['Total_Marks'] = np.sum(df[subjects], axis=1)
    df['Average_Marks'] = np.mean(df[subjects], axis=1).round(2)

    # Use loops where iteration is required to assign grades and status
    grades = []
    statuses = []
    
    for index, row in df.iterrows():
        grade = assign_grade(row['Average_Marks'])
        status = check_pass_fail(row['Average_Marks'], row['Attendance_Pct'])
        grades.append(grade)
        statuses.append(status)

    df['Grade'] = grades
    df['Status'] = statuses

    # Step 4: Perform Analysis
    # Answer practical questions and generate statistics
    print("--- Performance Analysis ---")
    
    # Highest, lowest and average performance
    highest_avg = np.max(df['Average_Marks'])
    lowest_avg = np.min(df['Average_Marks'])
    class_average = np.mean(df['Average_Marks']).round(2)
    
    print(f"Class Average: {class_average}")
    print(f"Highest Average: {highest_avg}")
    print(f"Lowest Average: {lowest_avg}")

    # Pass/Fail statistics
    total_passed = len(df[df['Status'] == 'Pass'])
    total_failed = len(df[df['Status'] == 'Fail'])
    print(f"\nPass/Fail Statistics: {total_passed} Passed, {total_failed} Failed")

    # Subject-wise performance analysis
    print("\n--- Subject-wise Performance (Average Marks) ---")
    for sub in subjects:
        sub_avg = np.mean(df[sub]).round(2)
        print(f"{sub.replace('_Marks', '')}: {sub_avg}")

    # Identify top-performing students
    print("\n--- Top Performing Student(s) ---")
    top_students = df[df['Average_Marks'] == highest_avg]
    for index, row in top_students.iterrows():
        print(f"Name: {row['Name']} | Department: {row['Department']} | Marks: {row['Total_Marks']}")

    # Step 5: Final Output
    print("\n--- Processed Student Data (Top 5 Rows) ---")
    print(df[['Name', 'Total_Marks', 'Average_Marks', 'Grade', 'Status']].head())

if __name__ == "__main__":
    main()
