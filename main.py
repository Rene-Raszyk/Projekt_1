
"""
main.py: první projekt do Engeto Online Python Akademie

author: Rene Raszyk
email: 2004reno2004@gmail.com
"""


TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]
users = ("bob", "ann", "mike", "liz")
passwords = ("123", "pass123", "password123", "pass123")
# print(type(passwords))


user_name = input("\nusername: ")
user_password = input("password: ")
n=0

for name in users:
    
    if name == user_name and user_password == passwords[n]:
        print("----------------------------------------")
        print("Welcome to the app,", user_name)
        print("We have 3 texts to be analyzed.")
        print("----------------------------------------")
        break
    n += 1
else:
    print("unregistered user, terminating the program..\n")
    exit()


druh_text = int()
druh_text = input("Enter a number btw. 1 and 3 to select: ")
print("----------------------------------------")


if not druh_text.isdigit():
    print("Wrong number, terminating the program..")
    exit()
if not 1 <= int(druh_text) <= 3:
    print("Wrong number, terminating the program..")
    exit()



druh_text = int(druh_text) - 1

pocet_slov = 0
pocet_vsech_slov = 0
pocet_velkych_slov = 0
pocet_malych_slov = 0
delka = 0
pocet_vseho_velkyho = 0
pocet_cisel = 0
suma_cisel = 0
cetnosti = {}

slova = TEXTS[int(druh_text)].split(" ")

for pocet in slova:

    pocet = pocet.strip(".?,!-\n")
    delka = len(pocet)

    if delka == 0:
        #print(pocet, delka)
        continue
    else:

        if pocet.isupper():
            pocet_vseho_velkyho += 1
            pocet_vsech_slov += 1

        if pocet.istitle():
            pocet_vsech_slov += 1
            pocet_velkych_slov += 1

        if pocet.islower():
            pocet_vsech_slov += 1
            pocet_malych_slov += 1

        if pocet.isnumeric():
            pocet_vsech_slov += 1
            pocet_cisel += 1
            suma_cisel = suma_cisel + int(pocet)

        #delka = len(pocet)
        if delka in cetnosti:
            cetnosti[delka] = cetnosti[delka] + 1
        else:
            cetnosti[delka] = 1
        
        #print(pocet, delka)

#print(slova)

print("There are",pocet_vsech_slov,"words in the selected text.")
print("There are",pocet_velkych_slov,"titlecase words.")
print("There are",pocet_vseho_velkyho,"uppercase words.")
print("There are",pocet_malych_slov,"lowercase words.")
print("There are",pocet_cisel,"numeric strings.")
print("The sum of all the numbers",suma_cisel)
print("----------------------------------------")
print("LEN|  OCCURENCES  |NR.")
print("----------------------------------------")

huhu = len(cetnosti) + 1
pocet = 1
#print(huhu)
#print(cetnosti)
mezera = " "
mezera_text = " "
star = "*"
string_stars = str()

for pocet in range(min(cetnosti), huhu):
    cislo_cetnosti = cetnosti[pocet]

    for _ in range(cislo_cetnosti):
        string_stars = string_stars + star
    
    if pocet < 10:
        mezera_text = mezera_text + mezera
    
    print(f"{mezera_text}{pocet}| {string_stars:<20} |{cetnosti[pocet]}")
    
    string_stars = ""
    mezera_text = " "
    
print("\n")