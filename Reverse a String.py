print("\033c")

string = input("enter a string: ")
rev_string = ""

for i in string :
    rev_string = i + rev_string

print(f"\noriginal string : {string}")
print(f"\nrevesed string : {rev_string}")