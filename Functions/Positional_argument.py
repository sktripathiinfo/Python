def total_marks(maths, science, english, hindi, history):
    total = maths + science + english + hindi + history
    print(total)

total_marks(89,74,45,43,56)

# named argument
total_marks(english=76,maths=83,history=67,hindi=56, science=81)
