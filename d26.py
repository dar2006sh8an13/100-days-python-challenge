#set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("union:", set1 | set2)
print("intersection:", set1 & set2)
print("difference :", set1 - set2)
print("symmetric difference:", set1 ^ set2)
print("is subset:", set1.issubset(set2))
print("is superset:", set1.issuperset(set2))
print("is disjoint:", set1.isdisjoint(set2))
print("add element to set1:")
set1.add(6)
print(set1)
print("remove element from set2:")
set2.remove(8)
print(set2)
print("length of set1:", len(set1))
print("clear set2:")
set2.clear()
print(set2)
