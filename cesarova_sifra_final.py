
while True:
    plaintext = input("Jaky text chces zasifrovat? ")
    if plaintext.isdigit():
        print("Sifrovat muzes pouze text.")
        plaintext = input("Zkus zadat text znovu: ")
    key = (input("Zadej klic podle ktereho budeme sifrovat, pouzij cisla 1-26: "))
    if not key.isdigit():
        print("Jako klic muzes zadat pouze cele kladne cislo mezi 1-26.")
        key = input("Zkus zadat klic znovu: ")        
        break

ciphertext = list() 

for char in plaintext:
    ciphertext.append(chr(ord(char) + int(key)))

print("Zakodovana sifra je", *ciphertext)



