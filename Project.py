print("Type negative numbers example -1")

x=(input("Enter a number:"))
sum=""
y=len(x)-1

while y >= 0:
 sum = sum + x[y]
 y = y - 1

print("\nReversed number is =",sum)