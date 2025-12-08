#sort characters by frequency
st = "tree"
for i in set(st):
    print(f"{i}"*st.count(i), end='')
