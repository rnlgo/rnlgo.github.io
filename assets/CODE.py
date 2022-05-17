import string

def rot13(message):
    return cesar(message, 13) # le chiffrement ROT13 est un cas particulier du chiffrement par césar avec 13 comme clé

def cesar(message, cle):
    cle = int(cle)
    message_crypte = ""
    for caractere in message: # on itère sur les caractères du message
        if caractere in string.ascii_lowercase: # si le caractère est une lettre minuscule (caractères accentués non inclus)
            index_caractere = string.ascii_lowercase.index(caractere)
            # on ajoute la clé, ensuite on utilise l'opérateur modulo "%" pour revenir au début si le résultat est > 26
            nouveau_caractere = string.ascii_lowercase[(index_caractere + cle) % 26]

            message_crypte += nouveau_caractere # on ajoute le caractère crypté au message
        elif caractere in string.ascii_uppercase:
            index_caractere = string.ascii_uppercase.index(caractere)
            nouveau_caractere = string.ascii_uppercase[(index_caractere + cle) % 26]

            message_crypte += nouveau_caractere
        else: # pas une lettre, on laisse le caractère tel quel
            message_crypte += caractere

    return message_crypte

def cesar_decode(message, cle):
    cle = int(cle)
    return cesar(message, -cle % 26)

def code_vigenere(message, cle):
    cle = cle.lower()
    if not all(i in string.ascii_lowercase for i in cle):
        raise TypeError
    message_crypte = ""
    index_cle = 0
    for i in range(len(message)):
        char_cle = cle[index_cle % len(cle)]
        decal = string.ascii_lowercase.index(char_cle) % 26

        caractere = message[i]

        if caractere in string.ascii_lowercase:
            index_caractere = string.ascii_lowercase.index(caractere)
            nouveau_caractere = string.ascii_lowercase[(index_caractere + decal) % 26]

            message_crypte += nouveau_caractere
            index_cle += 1
        elif caractere in string.ascii_uppercase:
            index_caractere = string.ascii_uppercase.index(caractere)
            nouveau_caractere = string.ascii_uppercase[(index_caractere + decal) % 26]

            message_crypte += nouveau_caractere
            index_cle += 1
        else:
            message_crypte += caractere
    return message_crypte

def code_vigenere_decode(message, cle):
    cle = cle.lower()
    if not all(i in string.ascii_lowercase for i in cle):
        raise TypeError
    return code_vigenere(message, "".join(chr(ord('z')-(ord(i)-ord('a')-1) % 26) for i in cle.lower()))

def code_polybe(message, cle):
    cle = int(cle) % 25
    message_code = ""
    table = string.ascii_lowercase
    table = table[cle:] + table[:cle]
    table = table.replace('j', '')
    for caractere in message.lower().replace('j', 'i'): # on itère sur les caractères du message
        if caractere in table:
            index = table.index(caractere.lower())
            message_code += f"{(index // 5)+1}{(index % 5)+1}"
    return message_code

def code_polybe_decode(message, cle):
    cle = int(cle) % 25
    message_decode = ""
    table = string.ascii_lowercase
    table = table[cle:] + table[:cle]
    table = table.replace('j', '')
    for i in range(0, len(message), 2):
        char = message[i:i+2]
        message_decode += table[(int(char[0])-1)*5 + int(char[1])-1]
    return message_decode

def code_polybe_variante(message, cle):
    cle = int(cle) % 36
    message_code = ""
    table = (string.ascii_lowercase + string.digits)
    table = table[cle:] + table[:cle]
    for caractere in message.lower(): # on itère sur les caractères du message
        if caractere in table:
            index = table.index(caractere.lower())
            message_code += f"{(index // 6)+1}{(index % 6)+1}"
    return message_code
def code_polybe_variante_decode(message, cle):
    cle = int(cle) % 36
    message_decode = ""
    table = (string.ascii_lowercase + string.digits)
    table = table[cle:] + table[:cle]
    for i in range(0, len(message), 2):
        char = message[i:i+2]
        message_decode += table[(int(char[0])-1)*6 + int(char[1])-1]
    return message_decode
