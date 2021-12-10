n = int(input("Enter your numbers:"))
counter = 0
for i in range(1, n+1):
    if n % i == 0:
        counter = counter + 1
if counter == 2:
    print("adad aval ast")
else:
    print("adad aval nist")
