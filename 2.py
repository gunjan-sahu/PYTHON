'''
#String
a='Hello Sir'
b='World'
c=a.split()
d=b.replace('World','Universe')
print(c,d)


#F-String
name='Gunjan'
branch='cse'
print(f"Hello myself {name} and currently in {branch}")


#List
l=[1,2,3,5,7,9,10]
l.extend([4,6,8])
l.sort()
print(l)
l.remove(1)
print(l)
l.sort(reverse=True)
print(l)
l.pop()
print(l)


#Tuple
t=(11,12,13,14,15,16,20)
r=t.index(16,2,)
print(t)
print(r)
'''

#Set has {}
#Dict has {}. It has key and values. Values can be duplicated but keys's can't be

#Set is unordered, un-indexed and un changeable. It does  not store duplicate values.
#True and 1 are same in sets. False = 0

m_set={'maths','dstl','physics'}
print(m_set)

n_set={'coa','science','english','science'}
print(n_set)

o_set={'maths','dstl','physics',True,1,2}
print(o_set)
print(len(o_set))

m={1,5,6,8,3}
print(type(m))

#add item
o={'coa','science','english','science'}
o.add('physics')
print(o)

o.update(m_set)
print(o)