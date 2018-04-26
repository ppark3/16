def union(a, b):
    newList = [i for i in a if i not in b] + b
    return newList

print union([1,2,3], [2,3,4])
print union([1,6,9,10],[6,7,8])

def intersection(a, b):
    newList = [i for i in a if i in b]
    return newList

print intersection([1,2,3], [2,3,4])

def set_difference(a, b):
    newList = [i for i in a if i not in b]
    return newList

print set_difference([1,2,3], [2,3,4])

def symmetric_difference(a,b):
    newList = [i for i in a if i not in b] + [i for i in b if i not in a]
    return newList

print symmetric_difference([1,2,3], [2,3,4])

def cartesian_product(a,b):
    newList = [(i,j) for i in a for j in b ]
    return newList

print cartesian_product([1,2],['red','white'])
