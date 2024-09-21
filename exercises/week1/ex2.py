"""
## Uppgift 2

Skriv ett program som skriver ut frekvensen av tecken i en given sträng.
Exempel-input: "banana"
Förväntad output: {"b":1, "a":3, "n":2}
"""




def teckenfrekvens(strang):
    frekvens = {}  # Skapa en tom ordlista för att hålla frekvensen av tecken

    # Gå igenom varje tecken i strängen
    for tecken in strang:
        if tecken in frekvens:
            frekvens[tecken] += 1  # Om tecknet redan finns, öka räkningen
        else:
            frekvens[tecken] = 1   # Om tecknet inte finns, sätt värdet till 1

    return frekvens

# Exempelanvändning
strang = "banana"
resultat = teckenfrekvens(strang)
print(resultat)