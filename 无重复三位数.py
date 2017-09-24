a = []
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and j != k and i != k :
                a.append(print(i,j,k))
print(len(a))
                
                
