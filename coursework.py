#Q1. Write a Python program to replace last value of tuples in a list.
#Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

#Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]


l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print([t[:-1] + (100,) for t in l])

#Q2. You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

string = input("Enter String:")

print(string.swapcase())   
#Q3. The user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

s = input("Enter String:")
sb = input("Enter Sub-String:")
results = 0
sub_len = len(sb)
for i in range(len(s)):
    if s[i:i+sub_len] == sb:
        results += 1
print(results) 

#Q.4 Write a class in which its one method accepts a string from console and 
#another method to print the characters that have even indexes.
class Print:
     def __init__(self):
       self.string=""
     def get(self):
       i = input("Enter the characters:")
       for index in range(len(i)):
           #checks the even indexes and print it
           if(index % 2 == 0):
               print(i[index], end="") 
obj = Print()
obj.get()