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


def final_stack(sci_fi, crime_fiction, fantasy, comics):

    final_pila = []

    clase_stack = [sci_fi, crime_fiction, fantasy, comics, comics]


    while True:

        #Each iteration until exit condition is met
        for pila in clase_stack:
            if pila:
                final_pila.append(pila.pop(-1))

         #exit condition
        if not sci_fi and not crime_fiction and not fantasy and not comics:
            break

    return final_pila


if __name__ == "__main__":
    pila1 = final_stack(sci_fi, crime_fiction, fantasy, comics)
    print_stack(pila1)



#clase_stack = ["sq_scifi", "sq_fantasy", "sq_crime_fiction", "sq_comics", "sq_comics"]

#print(sci_fi.pop(-1), " ", crime_fiction.pop(-1), " ", fantasy.pop(-1), " ", comics.pop(-1)," ", comics.pop(-1))











"""
e = sq_comics.pop(1)
print_queue(sq_comics, "Queue after deleting another element:",
            "The element removed was: {}".format(e))
"""
#print(sci_fi_last, " ", crime_fiction_last, " ", fantasy_last ," ", comics_last, " ", comics_last_2)



