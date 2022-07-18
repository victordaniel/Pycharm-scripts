node_from=[1,2,3,4,5,6]
node_to=[1,2,6,7,8]
d=dict()
for i in range(0,12):
    d[i]=[]
for(i,j) in zip(node_from,node_to):
    if j not in d[i]:
        d[i].append(j)
    if i not in d[j]:
        d[j].append(i)

for i in range(0,12):
    print(d[i])
