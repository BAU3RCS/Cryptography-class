p=2039
alpha=73
q=(p-1)/2
a=1337
#b is the other person's random num

public_key=pow(alpha,a,p)
print(public_key)

public_key2=753
session_key=pow(public_key2,a,p)

print(session_key)

#small brute force
for x in range(2,p):
    if pow(alpha,x,p)==public_key2:
        print("private key is: ",x)
        break

