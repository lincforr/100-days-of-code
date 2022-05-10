# 100 Days of Code Day 009

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Bug"])

programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary["Loop"])

# empty_dictionary = {}

# Wipes dictionary
# programing_dictionary = {}

programming_dictionary["Bug"] = "A moth in your computer"

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
