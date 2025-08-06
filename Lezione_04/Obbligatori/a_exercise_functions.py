'''
Suppose that you need to find the sum of integers from 1 to 10, 20 to 37, and 35 to 49. Write a Python program that
compute these three different sums.
'''

# # sum of integers from 1 to 10
# sum:int = 0

# for i in range(1, 11):
#     sum += i

# print("Sum from 1 to 10 is", sum)

# # sum of integers from 20 to 37
# sum:int = 0

# for i in range(20, 38):
#     sum += i

# print("Sum from 20 to 37 is", sum)

# # sum of integers from 35 to 49
# sum:int = 0

# for i in range(35, 50):
#     sum += i

# print("Sum from 35 to 49 is", sum)

def sum(a: int, b: int) -> int:

    result: int = 0

    for i in range(a, b+1):

        result = result + i

    return result

# si puo fare anche cosi
mysum = sum(1, 10)

# use sum function to compute a sum of integers from 1 to 10
print(f"Sum from 1 to 10 is {sum(1, 10)}")
# use sum function to compute a sum of integers from 20 to 37
print(f"Sum from 20 to 37 is {sum(20, 37)}")
# use sum function to compute a sum of integers from 35 to 49
print(f"Sum from 35 to 49 is {sum(35, 49)}")