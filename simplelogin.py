a=input()
result=""
for i in range(1,len(a)+1):
    result+=(a[len(a)-i])
print(result==a)