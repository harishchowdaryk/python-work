a={1,23,3,4,5}
b={4,5,8,7}
a.add(9)
a.pop()    #deleting randomly
a.remove(3)   #remove specified element
a.discard(23)  #same as remove but doest show any error
print(a.union(b),a,b)  #it will show both a and b and not changed in original set
print(a.update(b),a,b) #it will update to original set
print(a|b)  #union use operator
print(a.intersection(b))
print(a.intersection_update(b))
print(a&b)
print(a.difference(b))
print(a.difference_update(b))
print(a-b)
print(a.symmetric_differencedifference(b))
print(a.symmetric_difference_update(b))
print(a^b) #a(xor)b
print(a>=b)# to find superset of b
print(a.issuperset(b))
print(a.issubset(b))
print(a.isdisjoint(b))  #if no intersection return true




