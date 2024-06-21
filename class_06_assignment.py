# 1. Write a for loop to iterate through the student_scores dictionary and print each student's name and their score in the format: Student: [Name], Score: [Score].
#Solution

# student_scores = { "Alice": 85,"Bob": 78,"Charlie": 92,"Diana": 88, "Evan": 76}
# for i in student_scores:
#     print(f"Student: {i}, Score: {student_scores[i]}")

# 2. Write a for loop to calculate the average score of the students. Print the average score.
#Solution
# student_scores = { "Alice": 85,"Bob": 78,"Charlie": 92,"Diana": 88, "Evan": 76}
# sum_of_score = 0
# count = 0
# for score in student_scores.values():
#     sum_of_score += score
#     count +=1 

# avg_score = sum_of_score / count
# print(avg_score)    

# 3. Write a for loop to assign grades based on the following criteria:
# Score >= 90: Grade A
# Score >= 80 and < 90: Grade B
# Score >= 70 and < 80: Grade C
# Score < 70: Grade D
# Store these grades in a new dictionary called student_grades.

#Solution
# student_scores = { "Alice": 85,"Bob": 78,"Charlie": 92,"Diana": 88, "Evan": 76}
# student_grades = {}
# for student in student_scores:
#     if student_scores[student] >= 90:
#         grade = 'A'
#     elif student_scores[student] >= 80:
#         grade = "B"
#     elif student_scores[student] >= 70:
#         grade = "C"
#     else:
#         grade = "D"
#     student_grades[student] = grade 
# print(student_grades)                   


# 4. Modify the student_scores dictionary by adding 5 bonus points to each student's score. 
# Print the updated student_scores dictionary.
#Solution

# student_scores = { "Alice": 85,"Bob": 78,"Charlie": 92,"Diana": 88, "Evan": 76}
# for student in student_scores:
#     student_scores[student] += 5
# print(student_scores)    
    
# Create a dictionary named employee_data with the following key-value pairs:
# "John": 55000
# "Emma": 60000
# "Harry": 70000
# "Sophia": 65000
# "Mike": 48000

# 1. Write a for loop with an if statement to identify employees who earn more than $60,000. Print their names.
#Solution
# employee_data = {"John": 55000,"Emma": 60000,"Harry": 70000,"Sophia": 65000,"Mike": 48000}

# for employee in employee_data:
#     if employee_data[employee] > 60000:
#         print(employee)

# 2. Write a for loop to increase the salary of each employee by 10%. Update the dictionary accordingly.
#Solution
# employee_data = {"John": 55000,"Emma": 60000,"Harry": 70000,"Sophia": 65000,"Mike": 48000}
# for employee in employee_data:
#     employee_data[employee] += ((employee_data[employee] * 10) // 100)
# print(employee_data)    

"""
Create a dictionary named library_books with the following key-value pairs:
"The Great Gatsby": 4
"1984": 6
"To Kill a Mockingbird": 3
"The Catcher in the Rye": 5
"Moby Dick": 2

1. Write a for loop with range to add 2 more copies to each book. Update the dictionary accordingly.
"""
#Solution
# library_books = {"The Great Gatsby": 4,
# "1984": 6,
# "To Kill a Mockingbird": 3,
# "The Catcher in the Rye": 5,
# "Moby Dick": 2}

# for book in library_books:
#     library_books[book] += 2
# print(library_books)    

# 2. Write a for loop to calculate the total number of books in the library. Print the total count.
#Solution
# library_books = {"The Great Gatsby": 4,
# "1984": 6,
# "To Kill a Mockingbird": 3,
# "The Catcher in the Rye": 5,
# "Moby Dick": 2}
# total_books = 0
# for book in library_books:
#     total_books += library_books[book]
# print(total_books)    

"""
Write a for loop to assign book stock categories based on the number of copies available:
Copies >= 5: "Popular"
Copies >= 3 and < 5: "Available"
Copies < 3: "Limited"
Store these stock categories in a same dict i.e library_books.
"""
#Solution
# library_books = {"The Great Gatsby": 4,
# "1984": 6,
# "To Kill a Mockingbird": 3,
# "The Catcher in the Rye": 5,
# "Moby Dick": 2}

# for book in library_books:
#     if library_books[book] >= 5:
#         library_books[book] = "Popular"
#     elif library_books[book] >= 3:
#         library_books[book] = "Available"
#     else:
#         library_books[book] = "Limited"
# print(library_books)                


"""
Given the dict

students = {
    "Alice": {
                "Subjects": ["Math", "Science", "English"],
                "Scores": [85, 90, 78],
                "Class": 10
            },
    "Bob": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [75, 80, 88],
        "Class": 10
    },
    "Charlie": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [92, 89, 94],
        "Class": 11
    },
    "Diana": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [88, 76, 85],
        "Class": 11
    },
    "John": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [50, 60, 60],
        "Class": 11
    }
}
"""
students = {
    "Alice": {
                "Subjects": ["Math", "Science", "English"],
                "Scores": [85, 90, 78],
                "Class": 10
            },
    "Bob": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [75, 80, 88],
        "Class": 10
    },
    "Charlie": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [92, 89, 94],
        "Class": 11
    },
    "Diana": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [88, 76, 85],
        "Class": 11
    },
    "John": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [50, 60, 60],
        "Class": 11
    }
}
# 1. display Alice English Score
#Solution

# for student in students:
#     if student == "Alice":
#         for score in students[student]:
#             if score == "Scores":
#                 print(students[student][score][-1])


# 2. display Bob Class
#Solution
# for student in students:
#     if student == "Bob":
#         for score in students[student]:
#             if score == "Class":
#                 print(students[student][score])

# 3. display Charlie Math Score
#Solution

# for student in students:
#     if student == 'Charlie':
#         for marks in students[student]:
#             if marks == "Scores":
#                 print(students[student][marks][0])


# 4. display Diana's avg score
#Solution
# total_marks = 0
# count = 0
# for student in students:
#     if student == "Diana":
#         for score in students[student]:
#             if score == "Scores":
#                 for i in students[student][score]:
#                     total_marks += i
#                     count += 1
# print(total_marks//count)         

# 5. display John's all subject name and score with format: Student: [Name], Score: [Subject], Score: [Score]. 
#Solution
                              