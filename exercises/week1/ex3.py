## Uppgift 3
"""
Skriv ett program som för en given sträng skriver ut de två första och de två sista tecknen i strängen (på valfritt format)
Exempel-input: "banana"
Förväntad output: "ba na"
"""


def bana_na(strang):
    return strang[0:2]+ " " + strang[-2:] 
print(bana_na("banana"))