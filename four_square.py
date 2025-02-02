import re
 
def decipher(keys, ciphertext):
    plaintext = ""
    alpha=['A', 'B', 'C', 'D', 'E',
           'F', 'G', 'H', 'I', 'K',
           'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U',
           'V', 'W', 'X', 'Y', 'Z']
    
    for bigram in re.findall('..',ciphertext):
        try:
            i1 = keys[0].index(bigram[0])
            x1, y1 = i1%5, i1//5
            i2 = keys[1].index(bigram[1])
            x2, y2 = i2%5, i2//5
            plaintext+=(alpha[y1*5+x2]+alpha[y2*5+x1])
        except:
            plaintext+=".."
        
    return plaintext
 
#top right
k1=['M', 'A', 'I', 'S', 'E',
    'F', 'G', 'H', 'K', 'L',
    'N', 'O', 'P', 'Q', 'R',
    'T', 'U', 'V', 'W', 'X',
    'Y', 'Z', 'B', 'C', 'D']
 
#bottom left
k2=['S', 'T', 'A', 'N', 'L',
    'E', 'Y', 'Z', 'B', 'C',
    'D', 'F', 'G', 'H', 'I',
    'K', 'M', 'O', 'P', 'Q',
    'R', 'U', 'V', 'W', 'X']
 
 
keys = [k1, k2]
ciphertext = 'ENEAOTAQK...' # I shortened this part when sending as a message
print(decipher(keys, ciphertext))
