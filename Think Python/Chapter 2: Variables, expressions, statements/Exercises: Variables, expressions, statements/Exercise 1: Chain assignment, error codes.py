# Question 1: Can't assign integers to other values: SyntaxError: cannot assign to literal
n = 42
# 42 = n
print("Question 1: n assigned to 42:", n)
# print(42)

# Question 2: Chain assignment works for all variables
x = y = z = 1
print("Question 2: Chain assignment with three variables:", "\n",
      "x ==", x, "\n",
      "y ==", y, "\n",
      "z ==", z)

# Question 3: Semicolons signify statements on new lines
print("Question 3: Testing semicolon:", "Test 1"); print("Question 3: Testing semicolon:", "Test 2")

# Question 4: Periods at ends of lines cause SyntaxError: invalid syntax
# print("Test").

# Question 5: Python products don't use mathematical notation:
## NameError: xy not defined
# print(xy)
## SyntaxError: invalid syntax
# print(x y)