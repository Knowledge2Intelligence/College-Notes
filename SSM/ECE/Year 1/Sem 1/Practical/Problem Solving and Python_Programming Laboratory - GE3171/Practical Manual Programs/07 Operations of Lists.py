library = ['Books','Periodicals','Newspaper','Manuscripts','Maps','Prints','Documents','Ebooks']

print('Library: ',library)

print('first element: ',library[0])

print('fourth element: ',library[3])

print('Items in Library from 0 to 4 index: ',library[0:5])

print("3rd or -7th element: ",library[-7])

library.append("AudioBooks")
print("Library list after append(): ",library)

print('index of\'Newspaper\':',library.index('Newspaper'))

library.sort()
print('after sorting: ',library)

print('Popped elements is: ',library.pop(4))
print('after pop(): ',library)

library.remove("Maps")
print('after removing\'Maps\': ',library)

library.insert(2,'CDs')
print('after insert: ',library)

print('Number of Elements in Library list : ',library.count('Ebooks'))