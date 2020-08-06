import MasterDegreeDS.DS_programming.activity_1_stacks as ac

"""
Operate with the stack of activity 1
"""

stack_1 = ac.final_stack(ac.sci_fi, ac.crime_fiction, ac.fantasy, ac.comics)

"""
#Normal
new_list = []
for element in stack_1:
    new_list.append(element + "a")

#List comprehension

new_list = [element+"a" for element in stack_1]


print(new_list)
"""

new_list_1 = [element for element in stack_1 if " " in element]
#print(new_list_1)

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

new_list_2 = [element for element in stack_1 if hasNumbers(element)]
#print(new_list_2)

new_list_3 = stack_1[0:4]
print(new_list_3)

new_list_4 = stack_1[1::2]
print(new_list_4)