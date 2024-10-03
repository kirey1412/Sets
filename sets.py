a=[1,2,3]
sampleset=set(a)
print(sampleset)

print (a[2])
#Sets are not indexable

#Check if an element exist in a set
if 2 in sampleset:
    print("Yes")
else:
    print("No")

#Adding element to the set
sampleset.add(4)
print (sampleset)

#Removing element of the set
sampleset.remove(2)
print(sampleset)

#Avoiding error in unexisting element
sampleset.discard(6)
print(sampleset)

b={6,7,8,9,5}
c={1,2,3,4,5}

#Union means Addition of Sets
print(b.union(c))
print(b|c)

#Intersection
print(b.intersection(c))
print(b&c)

#Difference
print(b.difference(c))
print(c-b)

#Symmetric Difference
print(b.symmetric_difference(c))
print(b^c)
