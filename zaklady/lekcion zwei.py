print("Ahoj")
odpoved = input("cislo od kreditni karty s datumem expirace a tema funny 3 cislama ze zadu: ")

try:
    odpoved = int(odpoved)
    print(odpoved)
finally:
    odpoved = float(odpoved)
except:
    print("retarde")
    odpoved = 0
print(odpoved + 22)
