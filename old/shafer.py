#!/usr/bin/env python
#-*- coding: utf-8 -*-
nbr = 2
sol = []
alpha="abcdefghijklmnopqrstuvwxyz"
#cryptbuff="267525 !! 16041 10'56165683 533 184901 537267 23927756472 174 116524500 1756777 12467 1706017464787123, 12467 681121427... 2542 389 113797 540338 23668756658 101 479925301 5748 678862939133396 385 739645106, 55459 101 21260539301, 149 537267 409031 13812 149 140102958 1516965 1551238451 427609 17700496851. "
cryptbuff="1397803 14 48195211 1670240 19395 62631077351 20094108 46208 1257644 811 1251 42247273127 697952 43616 55359776 855 1323046484084 815760084 1749691977 23165947 1739557041 76056772393675 36242 75711293253960356 1115 2980227895822964 1283 34933628 1378532 75386251628048 783518 791819 14 2248595809466 1242 40131 694613 1576835 1250228 1175 958628 645756845519193808667321647775477622218 58648355260718 2721490350303578 1397803 47587423 1211 1390052 73252461756371 43616 26799 1257644 56766080 15148 1198498 888313916 40131 20094400 7439492854897463082630063250"
crypt=[int(x.strip()) for x in cryptbuff.replace("'"," ").replace(".","").replace("!","").replace(",","").replace("  "," ").split() if x.strip()!='']

def split2blocks(chain,n):
    #separe une chaine en bloc de n caracteres
    return [chain[i:i+n] for i in range(0, len(chain), n)]

def bin2mot(bin,decode):
    # decodage
    global sol
    res = ''
    for i in split2blocks(bin,5):
      try:
        res += decode[i]
      except:
          pass
    #print type(res)
    sol.append(res)
    #sol += " "
    return res

def prep(mot):
    # patterning pour avoir des blocs de 5 bits
    tmpmot = mot
    while len(tmpmot)%nbr !=0:
        tmpmot='0'+tmpmot
    return tmpmot


if __name__ == '__main__':
    # preparation des dicos
  while nbr < 16:
    decode = {}
    encode = {}
    sol = []
    for i in alpha:
        decode["{:05d}".format(int(bin(alpha.index(i)+1).replace('0b','')))] = i
        encode[i] = "{:05d}".format(int(bin(alpha.index(i)+1).replace('0b','')))
    # decryptage
    for i in crypt:
        mot=prep(str(bin(i).replace('0b','')))
        bin2mot(mot,decode)
    # solution
    #print int(''.join([encode[x] for x in 'lemotquondoitencoderetquejepreferepasmettreenclairquandmemesinonceseraitunpeuabuse']),2)
    nbr = nbr +1 
    print
    print sol
