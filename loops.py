# def count_positive(num=[]):
#     count=0
#     for i in num:
#         if i>0:
#             count+=1
#     return count

# print(count_positive([1, -2, 3, -4, 5, 6, -7, -8, 9, 10]))

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

# def sum_of_even(num,n):
#     sum=0
#     for i in range(0,n+1):
#         if num[i] % 2 == 0:
#             sum+=num[i]
#     return sum

# print(sum_of_even(numbers,len(numbers)-1))


# def print_table(n):
#     for i in range(11):
#         if i == 5:
#             continue
#         print(n*i)

# print_table(2)

# def rev_string(str):
#     rev=""
#     # for i in str:
#     #     rev = i + rev
#     # return rev
#     for i in range(len(str)):
#         rev 

# print(rev_string("abcd"))

# str="hello"
# for i in str:
#     print(i)


# def factorial(num):
#     fact=1
#     while(num>0):
#         fact*=num
#         num-=1
#     return fact

# print(factorial(5))

# while(True):
#     val=input("Please enter number between 0 - 10 to break this loop")
#     if int(val)>0 and int(val)<=10:
#         break


# def is_prime(num):
#     for i in range(2, num//2):
#         if num % i == 0:
#             return False
#     return True

# print(is_prime(13))


# def first_unique(str):
#     freq={}
#     for i in str:
#         freq[i] = freq.get(i) + 1 if bool(freq.get(i)) else 1
#     for key in freq:
#         if freq[key] == 1:
#             return key
#     return "-1"

# print(first_unique("leetcode"))

def unique_list(items=[]):
    for i in items:
        if items.count(i)>1:
            return i
    return "All Unique"
items = ["apple", "banana", "orange", "apple", "mango"]
print(unique_list(items))