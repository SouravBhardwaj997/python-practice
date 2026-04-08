# sq=[i*i for i in range(1,21)]
# print(sq)

# even_num = [ i for i in range(1,51) if i % 2 == 0]
# print(even_num)

# names=["john","sourav","jane"]
# uppercase_names=[i.upper() for i in names]
# print("uppercase_names",uppercase_names)

# str="sourav"

# vowels=[i for i in str if i in "aeiou"]
# print("vowels","".join(vowels))
# words = ["python", "is", "awesome"]
# words_len=[len(i) for i in words]
# print("words_len",words_len)

# filtered_num=[i for i in range(50) if i % 3==0 and i % 5==0]
# print("filtered_num",filtered_num)


# nums = [3, -1, 5, -7, 2]
# all_positive_num= [ i if i>0 else 0 for i in nums ]
# print("all_positive_num",all_positive_num)

# matrix = [[1,2], [3,4], [5,6]]

# flat_arr = [j for i in matrix for j in i]

# print("flat_arr",flat_arr)

# list_of_tupes=[(i,i*i) for i in range(11)]

# print("list_of_tupes",list_of_tupes)

# num=[1,1,1,2,2,3,3,4,5,2,4,6]

# uni_num={i for i in num}
# print("uni_num",uni_num)

# str = "hello world"

# str_list=[i for i in str if i != " "]
# print("str_list",str_list)

# words = ["apple", "banana", "kiwi"]

# words_dict={i:len(i) for i in words}
# print("words_dict",words_dict)

# odd_even_dict={i: "even" if i % 2 ==0 else "odd" for i in range(1,21)}
# print("odd_even_dict",odd_even_dict)

# matrix = [[1,2,3],[4,5,6]]
# # expected_out matrix = [ [1,4] , [2,5] , [3,6] ]

# transpose_matrix=[[row[i] for row in matrix ]  for i in range(len(matrix[0]))]

# print("transpose_matrix",transpose_matrix)

# nums = [1, 2, 3]

# all_pairs=[(i,j) for i in nums for j in nums if j != i]

# print("all_pairs",all_pairs)

# Create a list of prime numbers up to 50

# prime_nums=[i for i in range(1,51) for j in range(2,i//2) if i % j != 0 ]
# print("prime_nums",prime_nums)

# Create a dict where keys are numbers and values are their factorial

# print([i: i for i in range(5)])

# Transpose a matrix
# matrix = [[1,2,3],[4,5,6]] -> [ [1,4],
#                                 [2,5],
#                                 [3,6] ]


# matrix = [[1,2,3],[4,5,6]]

# transpose_matrix=[[row[i] for row in matrix ] for i in range(len(matrix[0])) ]

# print("transpose_matrix",transpose_matrix)

# nums=[1,2,3]

# pairs=[(i,j) for i in nums for j in nums if i != j]
# print("pairs",pairs)

# prime_nums=[i for i in range(1,51) for j in range(2,i//2) if i % j == 0  ]

# print('prime_nums',prime_nums)

# prime_nums=[]
# for i in range(1,6):
#     fact=1
#     for j in range(1,i+1):
#         fact*=j
#     prime_nums.append(fact)


# prime=[i for i in range(2,51) if all( i % j !=0 for j in range(2,i))]
# # prime = [i for i in range(2, 51) if all(i % j != 0 for j in range(2, i))]
# print("prime",prime)


# Create a dict where keys are numbers and values are their factorial
fact = [i for i in range(1,6)] 