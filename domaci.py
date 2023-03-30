'''
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Lucie Ihnatoliova
email: lih48279@gmail.com
discord: Lucie I#2395
'''


TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
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

accounts = {
    "Bob": "123", 
    "Ann": "pass123", 
    "Mike": "password123", 
    "Liz": "pass123"
    }

line = '-' * 57


#TODO LOGIN

# username = input("Please enter your name:")
# password = input("Please enter your password:")
# print(line)
# for name in accounts:
#     if name == username:
#         if password == accounts[name]:
#             print(f"Welcome to the app, {username}!\nWe have 3 texts to be analyzed.")
#             print(line)
#     elif username not in accounts:
#             print(f"User not registered!")
#             quit()


#TODO pick a text Pokud uživatel vybere takové číslo textu, 
# které není v zadání, program jej upozorní a skončí,
# pokud uživatel zadá jiný vstup než číslo, 
# program jej rovněž upozorní a skončí.

anal_text = input("Please pick a text between 1 and 3: ")
if anal_text.isdigit() == False:
    print("Text do not exist!")
    quit()
elif int(anal_text) < 1 or int(anal_text) > 4:
    print("Text do not exist!")
    quit()
else:
    print(line)


vycistena_slova = []
selected = TEXTS[int(anal_text) - 1]
#print(selected)


#TODO clean the words
for slovo in selected.split():
    ciste_slovo = slovo.strip(".,!?")
    vycistena_slova.append(ciste_slovo)

# TODO dic words occurence
# word_occurence = {}
# for slovo in vycistena_slova:
#     if slovo not in word_occurence:
#         word_occurence[slovo] = 1
#     else:
#         word_occurence[slovo] += 1 #zkraceny zapis: word_occurence[slovo] = word_occurence[slovo] + 1
# print(word_occurence)
# TODO pocet slov
pocet_slov = len(selected.split())
print(f"There are {pocet_slov} words in the selected text.")



# TODO počet slov začínajících velkým písmenem,
upper_w = 0
for upper in selected.split():
    if(upper[0].istitle()):
        upper_w += 1
print(f"There are {upper_w} titlecase words.")

# TODO pocet slov psanych velkymi pismeny

# TODO počet slov psaných malými písmeny,
lower_w = 0
for lower in selected:
    if(lower[0].islower()):
        lower_w += 1
print(f"There are {lower_w} lowercase words.")

# TODO počet čísel (ne cifer),
count_alpha = 0 
for alpha in selected.split():
    if alpha.isnumeric() and not alpha.isalpha:
        count_alpha += 1
print(f"There are {count_alpha} numeric strings.")
    
print(type(selected.split()))

print(selected)
print(type(selected.split()))


# TODO sumu všech čísel (ne cifer) v textu.


























#Choose text and analyze

#choose_text = input("Enter a number between 1 and 3 to select:")
#if choose_text == "1":
     #print(TEXTS[0])
     #for words in (TEXTS[0]):
          #clean_words = words.strip(".,!?")
          #clean_words.append(clean_words.lower())



           

           
           
           
           



     










       

            






        




