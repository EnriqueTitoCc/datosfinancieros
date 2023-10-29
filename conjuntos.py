#conjunto=set(["dato1","dato3"])
#conjunto1=set(["dat1",("datlis1","datlis2")])
    
#print(conjunto1)
#incorporando una lista
conjunto2=frozenset(["n1","n2"])
conjunto3={conjunto2,"n3"}
print(conjunto3)

conjA={1,2,3,4,5,6}
conjB={2,4,6}
res1=conjB.issubset(conjA)
res2=conjA.issuperset(conjB)
res4=conjA.isdisjoint(conjB)
res3=conjB<=conjA
print(res1)
print(res2)
print(res3)
print(res4)

