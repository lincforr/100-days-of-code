# BOF

# def greet():
#     print("Hello")
#     print("How are you?")
#     print("How is the weather?")

# greet()

# def greet_with_name(name):
#     print(f"Hello {name}.".format())
#     print(f"How are you {name}?".format())

# greet_with_name(input("What is your name? "))

# def greet_with(name, location):
#     print(f"Hi {name}".format(name))
#     print(f"You live in {location}".format(location))

# # I do not live at the Sun JSYN ;)
# greet_with("runlevel", "Sun")

# Paint can chaldange

# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5

# area_wall = test_h * test_w
# paint_cans_needed = area_wall / coverage
# print(f"you need {paint_cans_needed} cans to cover your wall")

# Functions
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime == False:
        print("It's not a prime number")
    elif is_prime == True:
        print("It's a prime number")
    # is a prime
# Running code
n = int(input("Check this number: "))
prime_checker(number=n)

# EOF