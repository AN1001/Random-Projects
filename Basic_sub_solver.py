#very basic, may improve later on
cipher_text = """ZDL QTMJ CBNDV QTB ZDL VBMMNOXV FD QGOVKXVDX. ZDL KFXND, FD TMZ ZDL RONNB JXN VBFKNVKX, QJVL QTB ZDL RONNB JXN SDDOVNDN MQ ZDL GBVNKXN"""

def frequency_analysis(text):
    letters = {}
    just_text = text.replace(" ", "").replace(",", "").replace(".", "")
    
    for letter in just_text:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return {k: v for k, v in sorted(letters.items(), key=lambda item: item[1], reverse=True)}
    
most_common_letters = "etaoinshrdlcumwfgypbvkjxqz".upper()

frequencies = "".join(frequency_analysis(cipher_text).keys())

plaintext = ""
for letter in cipher_text:
    if not (letter in " ,."):
        index = frequencies.index(letter)
        plaintext += most_common_letters[index]
    else:
        plaintext += letter
    
print(plaintext)
