#Generates a different random string of 4 characters every time the program is run in one line (excluding this one :) )
print("".join(["abcdefghijklmnopqrstuvwxyz"[x] for x in [hash("asuf") % (26), hash("kajf") % (26), hash("jnew") % (26), hash("uiwe") % (26)]]))
