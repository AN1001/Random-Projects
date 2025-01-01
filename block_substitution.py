cipher = 'your cipher here'
block_length = 6
new = ""
h = {}
alpha = 'abcdefghijklmnopqrstuvwxyz'
for i in range(0,len(cipher),block_length):
   pair = cipher[i:i+block_length]
   if pair not in h:
       h[pair] = alpha[len(h)]
for i in range(0,len(cipher),block_length):
   pair = cipher[i:i+block_length]
   new+= h[pair]
print(new)
