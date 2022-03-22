# #Fibinachi seeries
# num = int(input("Enter the number:"))
#
# n1=0
# n2=1
# sum=0
# if num < 0:
#     print("Enter the value greater than 0")
# else:
#     for i in range (0, num):
#         n1=n2
#         n2=sum
#         sum = sum+n1
#         print(sum,end=" ")


#print natural numbers

# num = int(input("Enter the number:"))
# i =0
#
# while i<= num:
#     print(i)
#     i=i+1
#
# for age in range(1,5):
#
#     while age<=5:
#         if age==3:
#             continue
#         else:
#             print(age)
#         age=age+1
# print("Thanks")

#print Factorial number

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
n=int(input("Enter the value"))
res=factorial(n)
print(res)

