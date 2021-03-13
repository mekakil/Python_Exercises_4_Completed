"""
@Author:Victor Hugo de Barros
"""
prefixes = "JKLMNOPQ"
prefixes = list(prefixes)
prefixes1 = prefixes[5]
prefixes2 = prefixes[7]
suffix = "ack"

for letter in prefixes:
    if letter in (prefixes1):
        print(letter + 'u' + suffix)
    elif letter in (prefixes2):
        print(letter + 'u' + suffix)
    else:
        print(letter + suffix)