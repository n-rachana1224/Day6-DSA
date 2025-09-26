# def count_digits(n):
#     count=0
#     while n>0:
#         count=count+1
#         n=n//10
#     return count
# p=count_digits(100000)
# print("No of digits=",p)
#optimal Solution
import math
def count_digits(n):
    count=int(math.log10(n)+1)
    return count
print(count_digits(1000))





