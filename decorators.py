# Create a decorator to print the function name and the values of its arguments every time the function is called.


def func_info(func):
    def wrapper(*args,**kwargs):
        args_list=[i for i in args]
        kwargs_list=[i for i in kwargs.items()]
        print(f"function {func.__name__} is called with args {args_list} kwargs {kwargs_list}")
        result = func(*args,**kwargs)
        return result
    return wrapper

# @func_info
# def greet(name,greeting="hello"):
#     return f"{greeting}, {name}"


# print(greet("Sourav",greeting="hi"))

import time

# def timer(func):
#     def wrapper(*args,**kwargs):
#         start_time=time.time()
#         result=func(*args, **kwargs)
#         end_time=time.time()
#         print(f"{func.__name__} run from {start_time}-{end_time}")
#         return result
#     return wrapper

# @timer
# @func_info
# def func1():
#     time.sleep(4)    

# func1()

def cache_return(func):
    cache_values={}
    def wrapper(*args,**kwargs):
        key =" ".join([str(arg) for arg in args]) + " ".join([str(arg) for arg in kwargs.items()])

        # print("key",bool(cache_values.get(key)))
        if(cache_values.get(key)):
            return cache_values.get(key)
        result = func(*args,**kwargs)
        cache_values[key]=result
        return result
    return wrapper

@cache_return
def sum(a,b):
    time.sleep(4)
    return a+b

print("sum(3,4)",sum(3,4))
print("sum(3,4)",sum(3,4))
print("sum(3,4)",sum(2,4))
print("sum(3,4)",sum(3,4))
