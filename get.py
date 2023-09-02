with open('logs.txt', 'r') as f:
   y=f.readlines()
f = open("hasil.txt", "w")
f.write(f"".join(y[::-1]))
f.close()

print(" ".join(y[::-1]))


