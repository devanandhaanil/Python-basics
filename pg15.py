#patterns

for i in range(1,6):
    for j in range(i):
        print( i ,end=" ")
    print()


# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

for i in range(5,0,-1):
    for j in range(i):
        print( i ,end=" ")
    print()

# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1

for i in range(1,6):
    for j in range(1,i+1):
        print( j ,end=" ")
    print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


for i in range(5,0,-1):
    for j in range(i):
        print( "5" ,end=" ")
    print()

# 5 5 5 5 5
# 5 5 5 5
# 5 5 5
# 5 5
# 5


n=1
for i in range(1,6):
    for j in range(i):
        print( n ,end=' ')
    n=n+2
    print()

# 1
# 3 3
# 5 5 5
# 7 7 7 7
# 9 9 9 9 9



for i in range(1,5):
    for j in range(4-i+1):
         print( i ,end=" ")
    print()


# 1 1 1 1
# 2 2 2
# 3 3
# 4



