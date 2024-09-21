"""
## Uppgift 4

Skriv ett program som tar två strängar som input och skapar EN ny sträng där de två första tecken i varje sträng bytts ut.
Exempel-input: "abc", "xyz"
Förväntad output: "xyc abz
"""

def byta_tecken():
    strang1 = input("Enter the first string: ")
    strang2 = input("Enter the second string: ")
    firstletterchange = strang2[0] + strang1[1:] + " " + strang1[0] + strang2[1:]
    lastletterchange = strang1[0:-1] + strang2[-1] + " " + strang2[0:-1] + strang1[-1]

    return "first letter change " + firstletterchange + "And the last letter change " + lastletterchange

print(byta_tecken())