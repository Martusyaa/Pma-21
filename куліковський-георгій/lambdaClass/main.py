from person import Person
from random import randint
from uuid import uuid4 as rand_token


def main():
    lst = []    
    for i in range(10):
        lst.append(Person(str(rand_token()), randint(1, 201)))
    print(list(map(print, lst)))
    lst = list(map(lambda p : (str(rand_token()), randint(1, 21)), lst))
    print(list(map(print, lst)))

main()