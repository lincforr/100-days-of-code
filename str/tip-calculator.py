# Data types

# Strings

# print("Hello"[4])

# concatanated "123" and "345" into "123345"
# not 468 like you would think but if you used the function int()
# it would have worked
# print("123" + "345")

#Integers

# underscores can be used to seperate numbers like a comma for example
# 123,456,789 or 123_456_789 < thease underscoresare like commas
# print(123 + 345)


#Float

# 3.14159


#Boolean

# True and False are the only Boolean types
# True
# False

# Type Errors

# num_char = len(input("What is your name?"))
# this \/ does not work
# print("Your name has " + num_char + " characters")

# print("Your name has " + str(num_char) + " characters")

# a = float(123)
# print(type(a))

# print(70 + float("100.5"))
# print(str(70) + str(100))

# Arithmatic 

# \/ this is how you subtract
# 7 - 3

# you use a astrisc to multiply
# 3 * 2

# you use a forward slash to divide
# 6 / 3

# you can rase a number to a power by using two astriscs
# 2 ** 2

# this will give 7
# print(3 * 3 + 3 / 3 - 3)

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)


print(f"Each person should pay: ${final_amount}")
