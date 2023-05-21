import itertools

lista = []
lista_uzyt = input("Podaj litery, które chcesz dołączyć do listy (oddzielone spacją): ").split()
lista += lista_uzyt

with open("słownikV3.txt", "r", encoding="utf-8") as f:
    words = set(line.strip() for line in f)

matched_words = []

for n in range(3, 10):
    permutations = itertools.permutations(lista, n)
    for p in permutations:
        word = ''.join(p)
        if word in words:
            matched_words.append(word)

if len(matched_words) > 0:
    print("Dopasowane słowa:")
    for word in matched_words:
        print(word)
else:
    print("Nie znaleziono dopasowanych słów.")

print("\n")
print(len(matched_words))