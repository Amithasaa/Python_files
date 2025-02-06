#reverse() will reverse original object

li = [10,5,20,6,40]
print('Before reverse', li) #Before reverse [10, 5, 20, 6, 40]
li.reverse()
print('After reverse', li) #After reverse [40, 6, 20, 5, 10]

#reversed(iterable_object) : return iterable object
li2 = [11,6,8,22]
reverse_li2 = reversed(li2)
print(reverse_li2) #<list_reverseiterator object at 0x00000205FFE97280>

#list(reversed(object))
reverse_li2 = list(reversed(li2))
print(reverse_li2) #[22, 8, 6, 11]

li3 = [1,5,2,9]
new_rev = list(reversed(li3)) # creating new reversed list
li3.reverse #reversing original list
print(new_rev) #[9, 2, 5, 1]
print(li3) #[9, 2, 5, 1]