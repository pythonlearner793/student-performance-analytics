# 1. Project Title
Student Performance Analytics System.
**Student Name:** Jaskaran Singh Randhawa

# 2. Objective
The objective of this project is to build a Python-based Student Performance Analytics System. It solves the problem of manually calculating student grades and performance metrics by automating the reading, processing, and analysis of student records to output meaningful results like pass/fail statistics and top performers.

# 3. Technologies Used
*   **Python:** Main programming language.
*   **Pandas:** Used for loading the CSV, organizing the data into a DataFrame, and data manipulation.
*   **NumPy:** Used for numerical operations like calculating total sums and means across subjects.

# 4. Dataset Description
The dataset `students.csv` contains 15 student records. Important columns include `Student ID`, `Name`, `Department`, subject marks (`Math Marks`, `Science Marks`, `English Marks`), and `Attendance`. Realistic values were used for all fields.

# 5. Implementation
1.  **Data Loading:** Read `students.csv` using `pd.read_csv()`.
2.  **Processing:** Used `np.sum()` and `np.mean()` along axis 1 to calculate `Total_Marks` and `Average_Marks`.
3.  **Functions & Loops:** Created reusable functions `assign_grade` and `check_pass_fail` in a separate module. Used a `for` loop with `df.iterrows()` to apply these functions to every student record based on their specific average and attendance.
4.  **Analysis:** Used NumPy's `np.max()`, `np.min()`, and `np.mean()` to extract overall class metrics. Filtered the DataFrame to count passing students and locate top performers.

# 6. Key Features
*   Automated total and average calculations using NumPy arrays.
*   Modular grading logic and pass/fail evaluation via custom functions.
*   Detailed class summary including highest, lowest, and class average scores.
*   Subject-wise performance breakdowns.
*   Identification of the top-performing student(s).

# 7. Output
<img width="893" height="548" alt="image" src="https://github.com/user-attachments/assets/db845554-8ac5-450d-9f81-f4c2cff75ec7" />


# 8. Final Outcome
The project successfully loaded raw student data, processed it accurately without errors, and produced a clear terminal report displaying class averages, subject performance, pass/fail counts, and identified the top performer. The dataset is properly structured and understandable without needing to inspect the code.

# 9. Challenges & Learning
*   **Challenge:** Figuring out how to calculate row-wise sums across specific subject columns without hardcoding. 
*   **Solution:** Used Pandas column selection combined with `np.sum(axis=1)`.
*   **Learning:** Gained practical experience integrating Pandas DataFrames with NumPy numerical calculations and utilizing loops safely within data analysis workflows.

# 10. GitHub Repository
**Repository Link:** https://github.com/pythonlearner793/student-performance-analytics.git
