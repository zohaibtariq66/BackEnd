# Extracting Sublist from a List of Temperatures
# Objective: Given a list of daily temperatures for a month, extract the temperatures for a specific week (e.g., week 2).

# Solution
# temperatures = [22, 24, 20, 25, 23, 26, 24, 25, 27, 29, 30, 28, 26, 27, 24, 23, 22, 21, 25, 24, 26, 27, 29, 28, 26, 25, 24, 23, 22, 21]
# week_2_temperature = temperatures[7:14]
# print(week_2_temperature)

"""
Extracting a Substring from a Sentence
Objective: Given a sentence, extract and print a specific word using string slicing.
sentence = "The quick brown fox jumps over the lazy dog"
extract third word "brow"
"""
# Solution
# sentence = "The quick brown fox jumps over the lazy dog"
# extracted_word = sentence[10:14]
# print(extracted_word)


"""
Extracting a Sublist of Favorite Colors
Objective: Given a list of favorite colors, extract a sublist of the first three colors using list slicing.
favorite_colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange"]
extract first three colors
"""
# Solution
# favorite_colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange"]
# extracted_colors = favorite_colors[:3]
# print(extracted_colors)

# Write a Python program to check if a list is empty or not.

# Solution
# list = []
# length_of_list = len(list)
# if length_of_list > 0:
#     print("List is Not Empty")
# else:
#     print("List is Empty")    

# 1. output the numbers from 1 to 10 using range function and for loop
# Solution

# for i in range(1,11):
#     print(i)

# 2. output the numbers from 35 to 50 using range function and for loop
# Solution

# for i in range(35,51):
#     print(i)

# 3. output the numbers from -15 to -25 using range function and for loop    
# Solution
# for i in range(-15, -26, -1):
#     print(i)
    
# 4. output the numbers from 5 to -10 using range function and for loop    
# Solution
# for i in range(5,-11,-1):
#     print(i)

# 5. output the numbers from 0 to 50 incremented by 3 using range function and for loop
# Solution

# for i in range(0,50,3):
#     print(i)

# 6.  Write a program to Generate Multiplication Table of 2 using range function and for loop
# Solution

for i in range(1, 11):
    print(f"2 x {i} = {2 * i}")