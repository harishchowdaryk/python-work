d={1:23,'a':23}
print(d.get('a'))
print(d.keys())
print(d.values())
print(d.items())
for i in d:
      print(i,d[i],end=" ")
for i,j in d.items():
      print(i,end=" ")