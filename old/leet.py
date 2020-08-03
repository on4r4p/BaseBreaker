def leet(txt):
     txt = txt.lower()
     txt = txt.replace("a","4").replace("b","8").replace("e","3").replace("g","6").replace("i","1").replace("l","1").replace("m","44").replace("o","0").replace("q","9").replace("r","|2").replace("s","5").replace("t","7").replace("z","2")
     return txt.upper()

while 1 == 1:
     print()
     toleet = str(input("Mot2leet :"))

     print()
     print("%s = %s"%(toleet,leet(toleet)))
     print()
