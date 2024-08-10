# Write a program to display index and the values (both) of a list using for loop. consider a list l = [100, 200, 300, 400]
#Solution
# my_list = [100, 200, 300, 400]

# for ind,val in enumerate(my_list):
#     print(ind,val)

# Write a program that find common values between 2 lists and also tells how many times the common value occurs.
# consider the list l1 = ['a', 'b', 'c', 'd'] and l2 = ['e', 'b', 'g', 'd', 'f', 'h']
#Solution
l1 = ['a', 'b', 'c', 'd'] 
l2 = ['e', 'b', 'g', 'd', 'f', 'h']
res = {}

for i in l1:
    res[i] = 1
    for j in l2:
        if j in res:
            res[j] += 1
        else:
            res[j] = 1 
            
print(res)
               