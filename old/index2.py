alpha =  ["","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

print("""Description :
La méthode suivante permet d'indexer simplement et automatiquement tous les mots alphabétiques d'un dictionnaire (On ne tient pas compte des caractères accentués).

Hint : le mot "VALIDER" fait partie du texte chiffré.

Épreuve :
267525 !! 16041 10'56165683 533 184901 537267 23927756472 174 116524500 1756777 12467 1706017464787123, 12467 681121427... 2542 389 113797 540338 23668756658 101 479925301 5748 678862939133396 385 739645106, 55459 101 21260539301, 149 537267 409031 13812 149 140102958 1516965 1551238451 427609 17700496851. 
""")
print("""A = 1. B = 2. C = 3. D = 4. E = 5. F = 6. G = 7. H = 8. I = 9. J = 10. K =11. L = 12. M = 13. N =14. O =15. P = 16. Q =17. R =18. S = 19. T = 20. U =21. V =22. W = 23. X =24. Y =25. Z = 26""")
print()

mot = input("Entre un mot :")
#mot = "mot"
lst = []
lng = len(mot)
res = 1

for ltr in mot:

    chiffre = alpha.index(ltr)
    lst.append(chiffre)

for nbr in lst:
          
          res += res * nbr


print("Equivalent en chiffre : ",res)

crypt = """267525  16041 10 56165683 533 184901 537267 23927756472 174 116524500 1756777 12467 1706017464787123 12467 681121427 2542 389 113797 540338 23668756658 101 479925301 5748 678862939133396 385 739645106 55459 101 21260539301 149 537267 409031 13812 149 140102958 1516965 1551238451 427609 17700496851"""

crypt = crypt.split(" ")


print("\nBase26 and beyond\n")

res2 = []
res3 = ""
res4 = ""
cnt = 0
for nbrs in crypt:
     if len(nbrs) >0:
       for nbr in nbrs:
            if cnt > 1:
                res3 += " "
                cnt = 0
            res3 += nbr
            res4 += nbr
            cnt = cnt +1   
#          print("%s = %s "%(nbrs,chr(int(nbrs))))
#          for nbr in nbrs:
#               ln = len(nbrs)
#               add = int(nbr) + len(nbrs)
#               moins = 26 - add
#               res2.append(alpha[moins])
          

#print(res2)
#print(res3)
print(res4)   


