import bcrypt, sys

password = "qwerty"
hash = sys.argv[1]
print("\n")
print(hash)
print("hu")
aFile = open("Top10kPasswords", "r")
for line in aFile:
    passw = line.rstrip().encode('utf-8')
    h = hash.encode('utf-8')
    if bcrypt.checkpw(passw, h):
        print("Found Password:" + line)
        quit()
print("no pass")