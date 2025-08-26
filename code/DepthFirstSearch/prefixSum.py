a = [1,6,2,5]
target = 7
preS = [0]*(len(a))
print(preS)

for i in range(len(a)):
    if i == 0:
        preS[i] = a[i]
    else:
        preS[i] = preS[i-1] + a[i]

res = []
lastIndex = -1
for i in range(len(preS)):    
    if preS[i] == target or preS[i] % target == 0:
        if i == 0:
            res.append([a[i]])
            lastIndex = i
        else:
            if lastIndex > -1:
                res.append(a[lastIndex+1:i+1])
                lastIndex = i
            else:
                res.append(a[0:i+1])
                lastIndex = i
print(res)

print(max(-3,-1))