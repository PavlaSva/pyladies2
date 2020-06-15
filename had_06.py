zvirata = ["had", "pes", "kocka", "kralik"]

zvirata.append("andulka")
zvirata.sort()
print(zvirata)

second_letters = {}
for zvire in zvirata:
    key = zvire[1]
    second_letters[key] = zvire

zvirata_dictionary = dict(second_letters)

for klic, zvire in sorted (zvirata_dictionary.items()):
    print(zvire)


