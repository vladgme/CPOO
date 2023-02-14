import random


# Get user input
name = 'Georgescu'
last_name = 'Vlad'

# Determine category based on age
for i in range(50):
    age = random.randint(0, 100)
    if age >= 9 and age <= 10:
        category = "Poussin"
    elif age >= 11 and age <= 12:
        category = "Benjamin"
    elif age >= 13 and age <= 14:
        category = "Minime"
    elif age >= 15 and age <= 16:
        category = "Cadet"
    elif age >= 17 and age <= 18:
        category = "Junior"
    elif age >= 19 and age <= 34:
        category = "Senior"
    elif age >=35:
        category = "Veteran"
    else:
        category = "Invalid age range"

    # Display user information and category
    print("Name:", name, last_name)
    print("Age:", age)
    print("Category:", category)
