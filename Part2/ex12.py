def calculate(a, op, b):
    if op =="+":
        return a + b 
    elif op =="-":
        return a - b 
    elif op =="*":
        return a * b 
    elif op =="/":
        return a / b 

print(calculate(10, "+", 10))
print(calculate(10, "-", 10))
print(calculate(10, "*", 10))
print(calculate(10, "/", 10))