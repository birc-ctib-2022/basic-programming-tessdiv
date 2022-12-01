import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
is_valid = False

if len(password) <16 or len(password) >=6: 
    lowercase = False
    uppercase = False 
    numeric = False
    character = False 
    for c in password:
        if c.islower() == True:
            lowercase == True 
        if c.isupper() == True: 
            uppercase == True
        if c.isnumeric() == True:
            numeric == True
        if c in "$#@":
            character == True
    if lowercase == True and uppercase == True and numeric == True and character == True: 
        is_valid == True    
print(is_valid)