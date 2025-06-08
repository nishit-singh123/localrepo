set1={10,34,87,87,1,"jenny",True}
set2=set()
set1.add(99)
set1.remove(10)
set1.discard(99)
set1.discard(106) # it will no show error as remove
print(set1.pop()) # i will remove any random item of range and give exception.
set1.clear()
set1.add((13,78,45,34)) # it will add immutable things.
set1.add([34,78,45]) # it will no add because list is mutable.
print(set1) # duplicate are not counted
print(type(set2))

# OPERATION
set1={"Ram","Shyam","jenny"}
set2={"Jenny","jiya","akash"}
set3={2,True,"Raghav","Shyam"}
print(set1.union(set2,set3)) #set1 must be a set but in argument you can pass list , tupple and it will convert into set then perform union on that iterable
print(set1.union("mohan","jenny"))
set2.union(set1)
print(set1 | set2) # operator for union and both operand should be a set.
set1.update(set2) # it will add element of set2 to set1 but no change in set1
set1.update(["jenny","mohan"])
set1|= set2
print(set1)
print(set1.intersection(set2,set3))
print(set1.intersection("mohan","shiva"))
print(set1 & set2) # operator of intersection
set1.intersection_update(set2) # it will update those item which is comman in set1 and set2.
print(set2)
print(set1)

# DIFFERENCE AND SYMMETRIC DIFFERENCE

print(set1.difference(set2,set3))
print(set1-set2) # with help of operator.
set2.difference_update(set2)
print(set1)
print(set2)
print(set1.symmetric_difference(set2,set3)) # two argument not allowed
print(set1^set2^set3) # apply on multiple sets
set1.symmetric_difference_update(set1)
set1.symmetric_difference_update(("mohan","shiva"))
print(set2)
print(set1)
print(set1.isdisjoint(set2))
print(set1.isdisjoint(['Mohan',"Shiva"]))
print(set1.issuperset(["mohan","shiva","jenny","Ram","Shyam"]))
print(set1<=set2)
print(set1>=set2)
set2.clear()
print(set2)
del set2


 





