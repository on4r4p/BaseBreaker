import re

## Converts text from format "1-2-3-4-5-6-7-8" to "abcdefgh"
## Sample input: "6-15-15-20-2-15-20 20-23-15: 7-18-21-14-11-12-5'19
## 7-18-5-22-5-14-7-5."

def A1Z26Cipher ( code ):
    return " ".join(
        ["".join([((re.search("\D", c).group(0)).join(
            [(chr(int(i)-1+ord('A'))) if i.isdigit() else ""
             for i in re.split("\D", c)]))
                  if not c.isdigit() else chr(int(c)-1+ord('A'))
                  for c in word.split("-")])
          for word in code.split(" ")])

def allsplit(s, i = 0):
  if len(s) == i:
    return [[s]]
  elif s[i] == " ":
           # Part A                                     # Part B
    return [[s[0:i]] + acc for acc in allsplit(s[i + 1:])] + allsplit(s, i + 1)
  else:
    return allsplit(s, i + 1)

final = []
joined = []
res = []

crypt = """1397803 14 48195211 1670240 19395 62631077351 20094108 46208 1257644 811 1251 42247273127 697952 43616 55359776 855 1323046484084 815760084 1749691977 23165947 1739557041 76056772393675 36242 75711293253960356 1115 2980227895822964 1283 34933628 1378532 75386251628048 783518 791819 14 2248595809466 1242 40131 694613 1576835 1250228 1175 958628 645756845519193808667321647775477622218 58648355260718 2721490350303578 1397803 47587423 1211 1390052 73252461756371 43616 26799 1257644 56766080 15148 1198498 888313916 40131 20094400 7439492854897463082630063250"""
crypt = crypt.split(" ")

for word in crypt:
  if len(word) < 18:
    word = " ".join(word)
    #word = "1 9 1 1 2 2 1 2 0"
    final = []
    joined = []
    res = []
    res = allsplit(word)

    for tojoin in res:
         tojoin = "".join(tojoin)
         tojoin = tojoin.replace(" ","-")
         joined.append(tojoin)
    for postfin in joined:
         postmp = ""
         for chunk in postfin.split("-"):
             cnt = 0
             for j in chunk:
                       if cnt >=2:
                             postmp += "-"
                             cnt = 0
                       postmp += j
                       cnt = cnt +1
             postmp += "-" 
         if postmp[-1:] == "-":
              postmp= postmp[:-1]
         good2go = 1
         addone = 0
         for finalcheck in postmp.split("-"):
              if int(finalcheck) == 0:
                   addone = 1
         if addone == 1:
              newval = []
              for nbr in postmp.split("-"):
                   plus1 = int(nbr) + 1
                   newval.append(str(plus1))
              postmp = "-".join(newval)

         for finalcheck in postmp.split("-"):
              if int(finalcheck) > 26:
                   good2go = 0
         if not postmp in final and good2go == 1:
              final.append(postmp)

    for i in final:
         print("\n",i)     
         print(A1Z26Cipher(i))
