# Write a program to check whether a person is eligible to vote or not?

# age = int(input("Enter Your Age: "))

# if age >= 18:
#     print("You Are Eligible to Cast Vote")
# else:
#     print("You Are Not Eligible to Cast Vote")
        
# Write a program to check char is vowel or not.

# char = input("Enter the letter: ")
# char = char.lower()

# if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
#     print("Charachter "+ char + " is a vowel")
# else:
#     print("Charachter "+ char + " is a consonant")
        
# Write a program to check the number is positive or negative. User input.

# num = int(input("Enter A Number: "))

# if num > 0:
#     print("Positive Number")
# else:
#     print("Negative Number")

# Write a program to check whether a number is odd or even?

# num = int(input("Enter A number: "))

# if num%2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")    
    
# Write a program to check whether a number is odd or even?

# marks = int(input("Enter your marks: "))

# if marks >= 80:
#     print("A+")
# elif marks >= 70:
#     print("A")
# elif marks >= 60:
#     print("B") 
# elif marks >= 40:
#     print("C") 
# else:
#     print("Fail")          
        

# Write a program to check whether a number is divisible by 7

# num = 56
# if num%7 == 0:
#     print("Number is divisible by 7")
# else:
#     print("Number is not divisible by 7")

# Write a program to check if year is leap year.
# year = 2000

# if (year%400 == 0) or (year%4==0 and year%100!=0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")

# Write a program to ask user its name and check whether name consists of 5 or more letters

# user_name = input("Enter Your Name: ")
# length_of_name = len(user_name)
# if length_of_name > 5:
#     print("The length of your name is more than five")
# elif length_of_name < 5:
#     print("The length of your name is less than five")
# else:
#     print("The length of your name is five")          

# first_number = int(input("Enter the First Number: "))
# second_number = int(input("Enter the Second Number: "))
# operator = input("Enter the operator to perfrom operation: ")

# if operator == "+":
#     print(first_number + second_number)
# elif operator == "-":
#     print(first_number - second_number)
# elif operator == "*":
#     print(first_number * second_number)  
# elif operator == "/":
#     print(first_number / second_number) 
# else:
#     print("Something went wrong!")             

# Write a program that accepts 1 input from user and check if the number is divisible by 2 and 3 both.

# user_inp = int(input("Enter the Number: "))
# if user_inp%2 == 0 and user_inp %3 == 0:
#     print(str(user_inp) + " is divisible by 2 and 3 both")
# elif user_inp%2 == 0:
#     print(str(user_inp) + " is only divisible by 2")
# elif user_inp%3 == 0:
#     print(str(user_inp) + " is only divisible by 3")   
# else:         
#     print(str(user_inp) + " is not divisible by 2 and 3 both")


# Write a program that accepts 2 inputs from user and check which number is largest.

# first_num = int(input("Enter first Number: "))
# second_num = int(input("Enter Second Number: "))

# if first_num > second_num:
#     print("Frist Number is greater than Second Number")
# else:
#         print("Second Number is greater than First Number")    

# Write a program that accepts 3 input from user and check which number is largest.

# first_num = int(input("Enter first Number: "))
# second_num = int(input("Enter Second Number: "))
# third_num = int(input("Enter Third Number: "))

# if first_num > second_num and first_num >third_num:
#     print("First Number is greater than second and third")
# elif second_num > first_num and second_num > third_num:
#     print("Second Number is greater than first and thir Number")
# else:
#     print("Third Number is greater than first and second")    

# Write a program that accepts 3 input from user and check the second largest.

# first_num = int(input("Enter first Number: "))
# second_num = int(input("Enter Second Number: "))
# third_num = int(input("Enter Third Number: "))


# if (first_num > second_num and first_num < third_num) or (first_num < second_num and first_num > third_num):
#     print("Second Largest is " + str(first_num))
# elif (second_num > first_num and second_num < third_num) or (second_num < first_num and second_num > third_num):
#     print("Second Largest is " + str(second_num))
# else:
#     print("Second Largest is " + str(third_num))


# Write a python program that accept user an input. The valid input should be of following
# - GREEN or gREEN or green etc 
# - RED or red or rEd etc 
# - YELLOW or yellow or yELlOw etc
# program should display the following message on checking above input
# Car is allowed to go
# Car has to wait
# Car has to stop
# invalid input

# user_input = input("Enter Current light: ")
# user_input = user_input.lower()  

# if user_input == "green" or user_input == "red" or user_input == "yellow":
#     if user_input == "green":
#         print("Car is allowed to go")
#     elif user_input == "yellow":
#         print("Car has to wait")
#     else:
#         print("Car has to stop")        
# else:
#     print("Invalid Input")    


"""
Write a program that takes two numbers as input and prints:

"First number is greater" if the first number is greater than the second number.
"Second number is greater" if the second number is greater than the first number.
"Both numbers are equal" if the two numbers are equal.
"""

# first_number = int(input("Enter First Number: "))
# second_number = int(input("Enter Second Number: "))

# if first_number > second_number:
#     print("First number is greater")
# elif second_number > first_number:
#     print("Second number is greater")
# else:
#     print("Both numbers are equal")        

# Write a program that takes a password as input and checks its strength:

# password = input("Enter password: ")
# lenght_of_password = len(password)

# if lenght_of_password > 12:
#     print("Strong Password!")
# elif lenght_of_password > 6:
#     print("Moderate Password!")
# else:
#     print("Weak Password!")        

"""
Write a program that takes an employee's salary and years of service as input. Calculate the bonus as follows:

If the years of service are less than 5, no bonus.
If the years of service are between 5 and 10, bonus is 10% of the salary.
If the years of service are more than 10, bonus is 20% of the salary.
Print the bonus amount.
"""

# salary = int(input("Enter Salary Amount!: "))
# years_of_exp = int(input("Enter Year of Experienc: "))

# if years_of_exp > 10:
#     print("Bonus Amount is :" + str((salary * 20)//100))
# elif years_of_exp <= 10 and years_of_exp > 5:
#         print("Bonus Amount is :" + str((salary * 10)//100))
# else:
#     print("No Bonus!")

"""
Write a program that takes the total amount of a purchase as input and applies a discount:

If the amount is less than $100, no discount.
If the amount is between $100 and $500, apply a 10% discount.
If the amount is more than $500, apply a 20% discount.
Print the final amount after the discount.

"""

# amount = int(input("Enter Purchase Amount!: "))

# if amount > 500:
#     print("Final Amount is: "+ str(amount - ((amount*20)//100)))
# elif amount <=500 and amount > 100:
#     print("Final Amount is: "+ str(amount - ((amount*10)//100)))
# else:
#     print("No discount is applicable!")

"""
Write a program that takes a person's age as input and prints the age group they belong to:

If the age is less than 13, print "Child".
If the age is between 13 and 19 (inclusive), print "Teenager".
If the age is 20 or above:
    If the age is less than 65, print "Adult".
    If the age is 65 or above, print "Senior".
"""

# user_age = int(input("Enter Your Age: "))

# if user_age >= 20:
#     if user_age >= 65:
#         print("Senior")
#     else:
#         print("Adult") 
# elif user_age >= 13 and user_age <20:          
#     print("Teenager")
# else:
#     print("Child")    
   
   
"""
Write a program that checks if a customer is eligible for a discount based on their membership status and purchase amount:

If the customer is a member:
    If the purchase amount is $50 or more, print "Eligible for 10% discount".
    Otherwise, print "Eligible for 5% discount".
If the customer is not a member:
    If the purchase amount is $100 or more, print "Eligible for 5% discount".
    Otherwise, print "No discount".
"""

# member = False
# amount = int(input("Enter Purchase Amount: "))

# if member:
#     if amount >= 50:
#         print("Eligible for 10% Discount") 
#     else:
#         print("Eligible fro 5% Discount")    
# else:
#      if amount >=100:
#          print("Eligible for 5% Discount") 
#      else:
#          print("No Discount")              


"""
create the same ATM machine program that we do in last class.
features:
    allow only affiliated_card if age < 60
    allow govt employee regardless of age and affiliated_card
    charge 10 Rs more if grade is less than 18
"""

# balance = 100
# affiliated_card = False 
# age = 65
# is_govt_employee = True
# grade = 19
# my_profit = 10

# withdraw_amount = 50

# if balance < withdraw_amount:
#     print("Insufficient Balance!")
# elif is_govt_employee:
#     if grade >= 17:
#         balance -= withdraw_amount
#         print(balance)
#     else:
#         balance -= withdraw_amount + my_profit
#         print(balance)
# elif affiliated_card and age < 60:
#     balance -= withdraw_amount
#     print(balance)    
# else:
#     print("You Are Not Eligible For This Transaction!")           