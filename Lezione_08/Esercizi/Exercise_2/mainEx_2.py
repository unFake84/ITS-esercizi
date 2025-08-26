from mathop import MathOperations

# # [2] interattivo
# user: int = int(input("ADD - 1 or 2 - MULTIPLY?\n>>"))

# if user == 1:
#     print("-" * 50)
#     print(*"SUM")
#     print(f"Result: {MathOperations.add(float(input('Enter 1st number: ')), float(input('Enter 2nd number: ')))}")
#     print("-" * 50)

# elif user == 2:
#     print("-"*50)
#     print(*"MULTIPLY")
#     print(f"Result: {MathOperations.multiply(float(input('Enter 1st number: ')), float(input('Enter 2nd number: ')))}")
#     print("-" * 50)

# else:
#     print("Not valid")

# [2] tests

# senza oggetto (self)
print(MathOperations.add(2, 2))
print(MathOperations.multiply(2, 2))

# con oggetto (self) <- op
op: MathOperations = MathOperations()
print(op.add(2, 2))
print(op.multiply(2, 2))