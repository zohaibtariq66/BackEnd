# Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.

#Solution

# from datetime import date,datetime

# class Person():
#     def __init__(self, name, country,date_of_birth):
#       self.name = name
#       self.coutry = country
#       self.date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d')

      
#     def cal_age(self):
#         today = date.today()
#         return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))

          
    
# person_1 = Person("Zohaib","Pakistan","2000-06-10")    
# print(person_1.cal_age())
 
 
# Write a Python program to create a calculator class. Include methods for basic arithmetic operations

#Solution

# class Calculator():
#     def __init__(self,num1,num2,operator):
#         self.num1 = num1
#         self.num2 = num2
#         self.operator = operator
        
#     def operation(self):
#         if self.operator == "+":
#             return self.num1 + self.num2
#         elif self.operator == "-":
#             return self.num1 - self.num2
#         elif self.operator == "*":
#             return self.num1 * self.num2
#         elif self.operator == "/":
#             return self.num1 / self.num2
                    
        
# calculate = Calculator(5,8,"+")
# print(calculate.operation())      


# Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.

#Solution

class Cart():
    items = []
    
    
    def add_item(self,item,price):
        self.items.append((item,price))
        
shop = Cart()
shop.add_item("Banana",50)          
        
            
              
        