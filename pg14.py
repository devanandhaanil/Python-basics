#convert case
n=input("ENTER THE STRING:")
for i in n:
    if i.islower()==True:
        print(i.upper(),end='')
    else:
        print(i.lower(),end='')