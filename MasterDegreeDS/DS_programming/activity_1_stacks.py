"""
Program to sort which books read first with some criteria:

* Non same thematic
* Order: sci_fi, crime_fiction, fantasy, comic
* Comics are exception, it can be red two in a row
* keep relative order

solo se puede usar pop() y append()

"""

# Las siguientes variables muestran el contenido de las 4 pilas temáticas delibros


sci_fi = ["Dune", "Fahrenheit 451", "Ender's Game", "Hyperion", "The Foundation Vol.3", "The Foundation Vol.2",
          "The Foundation Vol.1", "1984"]
fantasy = ["The Wise Man's Fear", "A Clash of Kings", "Malazan Book of the Fallen", "The Name of the Wind",
           "Lord of the Rings", "A Game of Thrones"]
crime_fiction = ["Murder on the Orient Express", "The Cartel", "The Girl with the Dragon Tattoo",
                 "The Cuckoo's Calling", "The Godfather"]
comics = ["The Avengers vol. 3", "Spiderman vol. 16", "Ghost Rider vol. 2", "Spiderman vol. 15",
          "John Constantine vol. 5", "Batman vol. 13", "Green Arrow vol. 1"]

print("Sci_fi books: ", len(sci_fi))
print("fantasy books: ", len(fantasy))
print("crime_fiction books: ", len(crime_fiction))
print("comics books: ", len(comics))


def print_stack(s, msg_bef=None, msg_after=None):
    # Definimos la función auxiliar print_stack, que nos permitirá
    # visualizar una pila
    if msg_bef:
        print(msg_bef)
    if len(s) == 0:
        max_len = 10
    else:
        max_len = max([len(e) for e in s]) + 4
    print("|" + " " * (max_len + 2) + "|")
    for e in s[::-1]:
        print("| " + e + " " * (max_len - len(e)) + " |")
        print("|" + "_" * (max_len + 2) + "|")
        print(msg_after + "\n" if msg_after else "\n")


stack_scifi = []
stack_fantasy = []
stack_crime_fiction = []
stack_comics = []

"""
for (book1, book2, book3, book4) in zip(sci_fi, fantasy, crime_fiction, comics):
    stack_scifi.append(book1)
    stack_fantasy.append(book2)
    stack_crime_fiction.append(book3)
    stack_comics.append(book4)
"""


#Create the stacks

for book in range(len(sci_fi)):
    stack_scifi.append(sci_fi[book])
for book in range(len(fantasy)):
    stack_fantasy.append(fantasy[book])
for book in range(len(crime_fiction)):
    stack_crime_fiction.append(crime_fiction[book])
for book in range(len(comics)):
    stack_comics.append(comics[book])


print_stack(stack_comics)