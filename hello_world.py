# Trying to test whether I can push code
print("Hello, world! 😁")
print("Coucou")


import random
# exemple de walrus operator pour compter jusqu'a 10
while (compteur := random.randrange(11)):
    if compteur == 10:
        print("10")
        break