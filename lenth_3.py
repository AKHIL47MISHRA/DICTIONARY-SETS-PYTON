# 4. What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?

s = set()
s.add(20)
s.add(20.0)
s.add('20')
len(s)   
print(s)# the answer of the output[{20, '20'}] is bcause of        the set always contain the mathemaical value equalily  like 20 is equal t 20.0 so set will count it only  once


