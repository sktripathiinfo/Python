def total_marks(maths, science, english, hindi, history):
    total = maths + science + english + hindi + history
    print(total)

# Use Case: Use positional arguments when the order of the arguments is clear and significant.

total_marks(89,74,45,43,56)

# named argument
# Use Case: Use named arguments to improve readability, especially when the
# function has multiple parameters or when calling the function with fewer arguments than it accepts.

total_marks(english=76,maths=83,history=67,hindi=56, science=81)



