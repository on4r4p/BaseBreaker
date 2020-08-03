from baseConverter import *

"""
Define custom symbols for base26
"""

# use all english alphabets as base26 symbols
base26 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
          'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
          'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# vanilla base10 symbols
base10 = ['0','1','2','3','4','5','6','7','8','9']

# get base10 value if 'HELLO' is a base26 value
print( baseXtoY( 'HELLO',
                 inputBaseSymbols = base26 ,
                 outputBaseSymbols = base10) )


# use all english alphabets in lower and uppercase as base52 symbols
base52 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
          'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
          'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
          'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
          's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# 'hElLo' is a base52 value
print( baseXtoY( 'HELLO',
                 inputBaseSymbols = base52 ,
                 outputBaseSymbols = base10) )


# We can even consider regular english sentences as values of a base system
# include space, period, comma to define symbols for english sentences
base55 = base52 + [' ', '.', ',' ]

print( baseXtoY( 'The quick brown fox jumps over the lazy dog',
                 inputBaseSymbols = base55 ,
                 outputBaseSymbols = base10) )

# default symbols sequence 
# listing symbols by continuing the hex symbols sequence, base 1 to base 36
default_symbols_seq = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
d = [ x for x in default_symbols_seq ]

def convertBase(inputNum, frm, to):
    return baseXtoY(inputNum, d[:frm], d[:to])

print( convertBase("2310",frm = 10, to =16))



