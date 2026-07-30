"Exercise 2.2: Funciones, Scope y Mutables"

total_match = 0
def first_match():
    global total_match
    total_match = total_match + 1
    print("Total matches found:", total_match)

first_match()
print("Total matches found:", total_match)