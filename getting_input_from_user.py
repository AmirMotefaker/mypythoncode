# Code by @AmirMotefaker

# Getting Input From User

# # Solution 1
# user_input = input("Enter your number:  ")

# print(int(user_input))

# # Output:
# # Enter your number:  12
# # 12

# # Enter your number:  12.1
# # Traceback (most recent call last):
# #   File "e:\A.Motefaker\ABC\Python\MyCode\getting_input_from_user.py", line 7, in <module>
# #     print(int(user_input))
# # ValueError: invalid literal for int() with base 10: '12.1'


# Solution 2
user_input = input("Enter your number:  ")

print(float(user_input))

# Output:
# Enter your number:  12.1
# 12.1

# Enter your number:  12
# 12.0

# Enter your number:  hello
# Traceback (most recent call last):
#   File "e:\A.Motefaker\ABC\Python\MyCode\getting_input_from_user.py", line 24, in <module>
#     print(float(user_input))
# ValueError: could not convert string to float: 'hello'