alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

word = "191122120"

cnt = 0
pos = 0
while cnt <= len(word):
     res = ""
     for chiffre in word:
          res+= alphabet[chiffre]
     print(res)     
