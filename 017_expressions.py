# The expression is the fundamental unit of computation in your program. It is
# the combination of data and operators (and some other things) to produce a
# result.
# 2 + 3

# @TASK: Try this using `python` in the terminal:

expr = (2 + 3) * 4
print(expr)

# As you can see, we can use brackets to control the order the expressions are
# evaluated.

# That handy "`python` in the terminal" thing is called the Python REPL. REPL
# stands for Read, Evaluate, and Print Loop. It reads the code you type in,
# evaluates the expression, prints the result, and then does that forever in a
# loop.

def add_one(num):
  return num + 1

expr2 = 2 + add_one(4) * 3  # Evaluates to 17
print(expr2)

# Calling a function is also an expression!

expr3 = add_one(add_one(add_one(add_one(add_one(add_one(1))))))
print(expr3)