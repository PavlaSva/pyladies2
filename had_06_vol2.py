zvirata_list = ["had", "pes", "kocka", "kralik"]

zvirata_list.append("andulka")

second_letters = {}
for zvire in zvirata_list:
    key = zvire[1]
    second_letters[key] = zvire

zvirata_dictionary = dict(second_letters)

for klic, zvire in sorted (zvirata_dictionary.items()):
    print(zvire)


