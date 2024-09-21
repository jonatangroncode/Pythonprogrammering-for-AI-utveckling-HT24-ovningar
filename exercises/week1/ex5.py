"""
## Uppgift 5

Skriv ett program som lägger till "ing" i slutet av en given sträng, om strängen är kortare än 3 tecken ska den lämnas ofärndrad.
Expempel-input: "Python"
Förväntad output: "Pythoning"
"""

def add_ing():

    ordet = input("Skriv in ett ord:")
    if len(ordet) >= 3:
        return ordet + "ing"
    else:
        return ordet
    

print(add_ing())