# PasswordProject
2nd Semester Major Project, Cybersecurity

A project to crack passwords, like the John the Ripper program

# Dependencies
The Top10K Passwords must be downloaded with the program because it depends on the text file to work for Dictionary

# Command Line Arguments
types:

-m : MD5

-s : SHA-256

-b : BCrypt

-p : PlainText

Methods:

-B : Brute Force **Only works with PlainText**

-D : Dictionary
# Formatting
python3 Password_Cracking.py [pasword] [opt arg 1] [opt arg 2]

python3 Password_Cracking.py qwerty

python3 Password_Cracking.py qwerty -p -D

python3 Password_Cracking.py d8578edf8458ce06fbc5bb76a58c5ca4 -D -m

python3 Password_Cracking.py 65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5 -s -D

python3 Password_Cracking.py $2y$10$i2Rbs2hRTCf46BwgfD9vg.NZY9JHCDAYhmi6yPKyv4LiG9HzxlPVm -D -b
