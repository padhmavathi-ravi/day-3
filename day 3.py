#exp no 1 merging two dictionaries
def Merge(dic1, dic2):
    return (dic2.update(dic1))
dic1={'a':2,'b':4}
dic2={'c':8,'d':9}
print(Merge(dic1,dic2))
print(dic2)

#exp no 2: remove a key from dictionary
myDict = {'a':1,'b':2,'c':3,'d':4}
print(myDict)
if 'a' in myDict:
    del myDict['a']
print(myDict)


#exp no 3: map two lists into a dictionary

keys=['red','green','blue',]
values= ['0001','0010','1010','0101']
color_dictionary =dict(zip(keys,values))
print(color_dictionary)


#exp no 4: finding the length of the string
n=len({1,2,3,4,5})
print("the length of the set is:",n)

#exp no 5: remove the intersaction of 2nd set from the 1st set
sn1 ={1,2,3,4,5}
sn2= {6,7,8,9,4}
print("original sets:")
print(sn1)
print(sn2)
print("remove the intersection of a 2nd set from the 1st set using difference():")
sn1.difference_update(sn2)
print(sn1)
sn1={1,2,3,4,5}
sn2={6,7,8,9,6}
print("remove the intersection of a 2nd set from the 1st set using -= operater:")
print(sn1-sn2)

