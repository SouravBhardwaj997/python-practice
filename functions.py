# def square(num):
#     return num*num

# print(square(12))

# def calculate(num1,num2):
#     return {
#         "sum":num1+num2,
#         "sub":num1-num2,
#         "mul":num1*num2,
#         "div":num1//num2
#     }

# print(calculate(12,2))

# def multiple(val1,val2):
#     # print(type) 
#     return val1 * val2

# print("multiple",multiple("hello", 2))

# def greet(username="there"):
#     return f"hey {username}"

# print(greet("sourav"))
# print(greet())

# cube = lambda x,y: x**y

# print(cube(3,2))

# def custom_sum(*args):
#     sum=0
#     for i in args:
#         sum+=i
#     return sum

# print(custom_sum(1,2,5))

#recursive function to calculate factorial

# def fact(num):
#     if num == 0:
#         return 1
#     return num * fact(num-1)


# print(fact(5))


# def adder(x):
#     def add(y):
#         return x + y
#     return add

# func1 = adder(2)
# print(func1(4))
# print(func1(4))