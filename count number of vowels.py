a=str(input("Enter the string:\n"))
s=("aeiou")
b=0
for i in a:
    if i in s:
        b=b+1
print(b)