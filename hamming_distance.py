#hamming distance
x=input("Enter binary number 1: ")
y=input("Enter binary number 2: ")
count = 0
if (len(x)==len(y)):
    for i in range(len(x)):
        if x[i]!=y[i]:
            count+=1
    print("Hamming distance:",count)
else:
    print("invalid")
