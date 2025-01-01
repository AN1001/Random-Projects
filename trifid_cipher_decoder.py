cipher_text = ""

block_size = len(cipher_text)

grids = """
abc
def
ghi

jkl
mno
pqr

stu
vwx
yz!
"""

grids = grids.replace("\n", "").replace(" ", "").upper()
cipher_text = cipher_text.upper()

def decode(grids, cipher_text, block_size):
    coords = []
    for char in cipher_text:
        cur = grids.index(char)
        coords.append([cur//9 + 1, (cur%9)//3 + 1, (cur%9)%3 + 1])
        
    transposed = ""
    for i in range(0,len(coords), block_size):
        mesh = "".join([''.join([str(y) for y in x]) for x in coords[i:i+block_size]])
        third = int(len(mesh)/3)
        a,b,c = (mesh[0:third], mesh[third:2*third], mesh[2*third:3*third])
        for index in range(len(a)):
            transposed+=(a[index]+b[index]+c[index])
        
    output = ""
    for i in range(0,len(transposed),3):
        cur_coord = [int(x)-1 for x in transposed[i:i+3]]
        position = cur_coord[0]*9 + cur_coord[1]*3 + cur_coord[2]
        output+=grids[position]
    print(output)
    return output

decode(grids, cipher_text, block_size)
decode(grids, cipher_text, 3)
decode(grids, cipher_text, 5)
