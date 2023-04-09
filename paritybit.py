#parity checker
x=input("Enter in format of 0's and 1's: ")
count = 0
for i in x:
    if i=='1':
        count=+1
if(count%2==0):
    print("Odd parity:", x+'1')
    print("Even parity:", x+'0')
else:
    print("Odd parity:", x+'0')
    print("Even parity:", x+'1')
