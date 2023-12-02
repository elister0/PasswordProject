import sys, hashlib, bcrypt

type = ""
method = ""
dict_file = ""

# functions


def set_type(t):
    global type
    type = t


def set_method(m):
    global method, dict_file
    method = m
    if m == "Dictionary":
        dict_file = ""


def check_type(c):
    if c == type:
        return True
    return False


# Checking if password was given. If the first argument is not a password and instead
# gives information about the password cracking process, quits program
# options are -p Plain text, -m MD5, -bc BCrypt, -s SHA256, -d Dictionary, -b Brute force
password = sys.argv[1]
if password in ['-p', '-m', '-b', '-s', '-D', '-B']:
    print("**No password given to crack.**")
    quit()

given_arguments = sys.argv[2:]

for arg in given_arguments:
    if arg == "-p":
        set_type("PlainText")
    elif arg == "-m":
        set_type("MD5")
    elif arg == "-b":
        set_type("BCrypt")
    elif arg == "-s":
        set_type("SHA-256")
    elif arg == "-D":
        set_method("Dictionary")
    elif arg == "-B":
        set_method("Brute Force")

if len(type) == 0:
    print("**No type given. Defaulting to PlainText**")
    set_type("PlainText")
if len(method) == 0:
    print("**No method selected. Defaulting to Dictionary.**")
    set_method("Dictionary")
if method == "Brute Force" and not (type == "PlainText"):
    print("**Not a possible combination. Brute Force is only compatible with PLainText**")
    quit()

if method == "Dictionary":
    d = open("Top10kPasswords")
    print("Searching the Dictionary...")
    for line in d:
        temp_line = line.rstrip().encode('utf-8')
        if check_type("MD5"):
            hashed_temp_line = hashlib.md5(temp_line)
            check = hashed_temp_line.hexdigest()
        elif check_type("SHA-256"):
            hashed_temp_line = hashlib.sha256(temp_line)
            check = hashed_temp_line.hexdigest()
        elif check_type("PlainText"):
            check = line.rstrip()
        elif check_type("BCrypt"):
            temp_hash = password.rstrip().encode('utf-8')
            bcrypt.checkpw(temp_line, temp_hash)

        if check == password:
            print("Password Found: " + line)
            quit()
    print("Password not found in dictionary.")
    quit()

if method == "Brute Force":
    print("Brute Forcing...")
    temp_pass = ""
    pass_without_whitespace = password.rstrip()
    possible_values = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    for x in pass_without_whitespace:
        for val in possible_values:
            if x == val:
                temp_pass += val
                if temp_pass == pass_without_whitespace:
                    print("Password Found: " + temp_pass)
                    quit()
    print("Unable to Find Password")
    quit()
