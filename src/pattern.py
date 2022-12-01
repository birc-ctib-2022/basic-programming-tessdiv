
# Print the pattern
#J= []
#for i in range (5):
#    J.append("*")
#    print (*J)
#for i in range (5):
#    J.pop ()
#    print (*J)

#ALSO WORKS
#T= []
#for i in range (5):
#    T.append(str("*"))
#    print (" ".join(T))
#for i in range(5):
#    T.pop ()
#    print(" ".join(T))

stars = []

for i in range(9):
    if i <= 4:
        stars.append('*')
        print(*stars)
    elif i > 4:
        stars.pop()
        print(*stars)
