# n1
# set1={1,2,3,4,5,6}
# set2={4,5,6,7,8,9}
# print(sum(set1.difference(set2)))

# n2
set1={'olma', 'anor', 'youtube', 'instagram', 'gilos'}
set2={'youtube', 'gilos', 'anor', 'BMW', 'Tesla', 'Nissan'}
set3={'gilos', 'olma', 'instagram', 'Tesla', 'Nissan'}

set1.intersection_update(set2)
set1.difference_update(set3)
print(set1)
