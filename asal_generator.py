def asal_mi():
    sayı=2
    for i in range(1,1001):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            yield i

            
for i in asal_mi():
    print(i)
