#!/usr/bin/env python
# -*- coding: utf-8 -*-


tralphabet = ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "i", "ı", "j", "k", "l",
              "m", "n", "o", "ö", "p", "q", "r", "s", "ş", "t", "u", "ü", "v", "y", "z"]
enalphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
              "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
endecoders = ["Ceasar", "A1Z26", "Atbash", "Vigénere", "combined"]
trdecoders = ["Sezar", "A1Z26", "Atbeş", "Vicenere", "bileşik"]
trstrings = ["şifre:", "anahtar:", "YÖNTEMLER", "devam?", "evet", "hayır", "şifreleme", "şifre çözme", "veya"]
enstrings = ["cipher:", "key:", "METHODS", "continue?", "yes", "no", "Encrypt", "Decrypt", "or"]
# placeholder b4 i learn to do xml's
retry = True


tratbash = {"a": "z", "b": "y", "c": "v", "ç": "ü", "d": "u", "e": "t", "f": "ş", "g": "s", "ğ": "r", "h": "p",
            "ı": "ö", "i": "o", "j": "n", "k": "m", "l": "l", "m": "k", "n": "j", "o": "i", "ö": "ı", "p": "h",
            "r": "ğ", "s": "g", "ş": "f", "t": "e", "u": "d", "ü": "ç", "v": "c", "y": "b", "z": "a"}

enatbash = {"a": "z", "b": "y", "c": "x", "d": "w", "e": "v", "f": "u", "g": "t", "h": "s", "i": "r",
            "j": "q", "k": "p", "l": "o", "m": "n", "n": "m", "o": "l", "p": "k", "q": "j", "r": "i",
            "s": "h", "t": "g", "u": "f", "v": "e", "w": "d", "x": "c", "y": "b", "z": "a"}


def encrypt_ceaser(text, num): 
    result = "" 
    for character in text:
        i = -1 
        for x in alphabet: 
            i += 1 
            if x == character: 
                break 
        if character in alphabet: 
            if (i + num) < len(alphabet):
                result += alphabet[i + num]
            else:
                result += alphabet[(i + num) - len(alphabet)] 
        else: 
            result += character 
    return result

def encrypt_a1z26_tr(sentence):
    result = ""
    for character in sentence:
        i = -1
        if character in tralphabet:
            for x in tralphabet:
                i += 1
                if x == character:
                    break
            result += "-"
            result += str(i)
        else:
            result += character
    return result 
     

def encrypt_a1z26_en(sentence):
    result = ""
    for character in sentence:
        i = -1
        if character in enalphabet:
            for x in enalphabet:
                i += 1
                if x == character:
                    break
            result += "-"
            result += str(i)
        else:
            result += character
    return result 
     

def encrypt_vigenere_en(keyword, sentence):
    keynumbers = []
    for character in keyword:
        i = -1
        for word in enalphabet:
            i += 1
            if character == word:
                break
        keynumbers.append(i)
    y = -1
    result = ""
    for char in sentence:
        if char in enalphabet:
            i = -1
            y += 1
            for word in enalphabet:
                i += 1
                if char == word:
                    break
            i += int(keynumbers[(y % len(keynumbers))])
            if i < 26:
                result += str(enalphabet[i])
            else:
                result += str(enalphabet[(i - 26)])
        else:
            result += char
    return result 
     

def encrypt_vigenere_tr(keyword, sentence):
    keynumbers = []
    for character in keyword:
        i = -1
        for word in tralphabet:
            i += 1
            if character == word:
                break
        keynumbers.append(i)
    y = -1
    result = ""
    for char in sentence:
        if char in tralphabet:
            i = -1
            y += 1
            for word in tralphabet:
                i += 1
                if char == word:
                    break
            i += int(keynumbers[(y % len(keynumbers))])
            if i < 29:
                result += str(tralphabet[i])
            else:
                result += str(tralphabet[(i - 29)])
        else:
            result += char
    return result 
     

def bin2dec(num):
    i = len(str(num))
    num = 0
    for bas in str(num):
        i += -1
        num += int(bas) * (2 ** i)
    return num


def decrypt_vigenere(text, keyword):
    key = []
    result = []
    i = -1
    text = text.lower()
    for keyletter in keyword:
        key.append(numinlistfirst(alphabet, keyletter))
    for cipherletter in text:
        if cipherletter == " ":
            cipherletter = cipherletter
        else:
            i += 1
        keynum = key[i % len(key)]
        decipherletter = decrypt_ceasar(cipherletter, 25 - keynum)
        result.append(decipherletter)
    return ''.join(result)


def isitin(tosearchin, element):
    if numinlistfirst(tosearchin, element) is not None:
        return True
    else:
        return False


def decrypt_combined(tocombine, text):
    if isitin(tocombine, "a1"):
        text = decrypt_a1z26(text)
    if isitin(tocombine, "at"):
        text = get_atbash(text)
    if isitin(tocombine, "vi"):
        print(decrypt_vigenere(text, input(strings[1])))
    elif isitin(tocombine, "ce"):
        ceasar(text)
    else:
        return text


def get_atbash(text):
    results = []

    for letter in text:
        if isitin(alphabet, letter) is True:
            results.append(alphabet[(numinlistfirst(alphabet, letter)) * -1])
        else:
            results.append(letter)
    return ''.join(results)


def decrypt_a1z26(text):
    hyphen = 1
    nums = []
    letters = []
    for character in text:
        if len(nums) == 0:
            nums.append("")
        if character == "-":
            hyphen += 1
        elif character == " " or character == "," or character == "." or character == "?" or character == "!" or \
                        character == ":":
            nums.append(character)
            hyphen += 1
        elif character == "'" or character == '"':
            hyphen += 1
            nums.append(character)
        elif len(nums) < hyphen:
            if len(nums) > 0:
                if not nums[-1] == "":
                    nums.append(str(character))
        elif nums[hyphen - 1] == " ":
            nums.append(str(character))
            hyphen += 1
        else:
            nums[hyphen - 1] += str(character)
    for i in range(0, len(nums)):
        if not isint(nums[i]):
            letters.append(nums[i])
        else:
            letters.append(alphabet[int(nums[i]) - 1])
    return ''.join(letters)


def isint(val):
    try:
        int(val)
        return True
    except ValueError:
        return False


def numinlistfirst(listtosearch, tosearch):
    nelement = 0
    for element in listtosearch:
        nelement += 1
        if element == tosearch:
            return nelement


def decrypt_ceasar(harf, displacement):
    if harf == " ":
        return harf
    elif numinlistfirst(alphabet, harf) is None:
        return harf
    else:
        return alphabet[(numinlistfirst(alphabet, harf) + int(displacement)) % len(alphabet)]


def printdecoders():
    n = 0
    for dec in decoders:
        n += 1
        print("[" + str(n) + "]   " + dec)


def ceasar(text):
    text = text.lower()
    for displacement in range(0, len(alphabet)):
        print(displacement + 1, end="")
        if displacement < 9:
            print(" ", end="")
        print(": ", end="")
        for chara in text:
            print(decrypt_ceasar(chara, displacement), end="")
        if len(text) < 33:
            if displacement % 3 == 2:
                print(end="\n")
            else:
                print("  |  ", end="")
        else:
            print(end="\n")
    for _ in [1, 2]:
        print(end="\n")


def runprog():
    retry = True
    while retry:
        print(strings[6], strings[8], strings[7] + ":")
        form = input()
        print("-" * 10 + "=" + strings[2] + "=" + "-" * 10, end='\n')
        printdecoders()
        print(end="\n")
        decoder = input()
        if form == strings[7]:
            if int(decoder) == 1:
                ceasar(input(strings[0]))
            elif int(decoder) == 2:
                print(decrypt_a1z26(input(strings[0])))
            elif int(decoder) == 3:
                print(get_atbash(input(strings[0])))
            elif int(decoder) == 4:
                print(decrypt_vigenere(input(strings[0]), input(strings[1])), end="\n")
            elif int(decoder) == 5:
                methodraw = input(strings[2].lower() + ":")
                i = 0
                methods = []
                for _ in methodraw:
                    if i % 2 == 1:
                        methods.append(methodraw[i - 1] + methodraw[i])
                    i += 1
                print(decrypt_combined(methods, input(strings[0])))
        else:
            if int(decoder) == 1:
                number = int(input("choose a number"))
                print(encrypt_ceaser(input(strings[0]), number))
            elif int(decoder) == 2:
                print(encrypt_a1z26(input(strings[0])))
            elif int(decoder) == 3:
                print(get_atbash(input(strings[0])))
            elif int(decoder) == 4:
                print(encrypt_vigenere(input(strings[0]), input(strings[1])), end="\n")
            elif int(decoder) == 5:
                print("")
        print(strings[3], end="\n")
        reply = input()
        if reply.lower == strings[5].lower():
            retry = False
        elif reply.lower() == strings[4].lower():
            retry = True
        else:
            retry = False


def decrypt_binary(text, parsenum):
    lastword = []
    for t in range(0, len(text) / parsenum):
        word = ""
        for n in range(1, parsenum):
            word += text[n + parsenum * t]
        lastword.append(word)


lang = input("language/dil:")
print(end="\n")
if lang == "tr":
    alphabet = tralphabet
    decoders = trdecoders
    strings = trstrings
elif lang == "en":
    alphabet = enalphabet
    decoders = endecoders
    strings = enstrings
runprog()
# Cihan Alperen Bosnalı
# 6 November 2017

