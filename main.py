nombres = [4, 7, 10, 15, 2, 12, 19, 27, 87]
c = 0
d = 0

for i in nombres:
    if i % 2 == 0:
        c+=1
    else:
        d+=1

print(f"Il y a {c} nombres pairs et {d} nombres impairs.")
