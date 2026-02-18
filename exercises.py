# EXERCISE 1: List & Indexing
students = ['Jessee', 'Tristan', 'Morgan']
def manage_students(list):
    print("\nEXERCISE 1 | List & Indexing:")
    first_student = list[0]
    last_student = list[2]
    print(first_student, last_student)
manage_students(students)

# EXERCISE 2: Loop and String Concatenation
foods = ('Salad', 'Steak', "Pie")
def combine_foods(foods):
    print("\nEXERCISE 2 | Loop and String Concatenation:")
    meal = ''
    for food in foods:
        meal += food
    return meal
print(combine_foods(foods))

# EXERCISE 3: Slicing Tuples
def slice_foods(foods):
    print("\nEXERCISE 3 | Slicing Tuples:")
    new_tupple = (foods[-2], foods[-1])
    print(type(new_tupple), new_tupple)
slice_foods(foods)

# EXERCISE 4: Dictionaries and String Formatting
def hometown_info(hometown):
    print("\nEXERCISE 4 | Dictionaries and String Formatting")
    return f"I was born in {hometown['city']} {hometown['state']}, which has a population of {str(hometown['population'])}"
hometown = {
    'city': 'Richmond',
    'state': 'London',
    'population': 195300
}
print(hometown_info(hometown))

# EXERCISE 5: Iterating Over Dictionary Items
def list_hometown_items(hometown):
    print("\nEXERCISE 5 | Iterating Over Dictionary Items:")
    hometown_items = []
    for key,val in hometown.items():
        hometown_items.append(f"{key} = {val}")
    print(hometown_items)
list_hometown_items(hometown)