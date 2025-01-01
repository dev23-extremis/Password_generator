student_score = [180,124,165,173,189,169,146]

# print(sum(student_score))

# sum = 0
# for i in student_score:
#     sum += i
# print(sum)

# max = 0
# for i in student_score:
#     if i > max:
#         max = i
# print(max)

# sum = 0
# for i in range(1,101):
#     sum += i
# print(sum)

import random
import random2
import string

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

choosed_number = random.choices(numbers, k=3)
print(choosed_number)
random.shuffle(choosed_number)
print(choosed_number)


