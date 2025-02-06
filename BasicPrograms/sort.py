#sort(): Arranging the elements in ascending or descending order

#Sort() modify the original list or object in ascending order
li = [10,5,3,20]
li.sort()
print(li) #[3, 5, 10, 20]

#Sort(reverse=True) modify the original list or object in descending order
li.sort(reverse=True)
print(li) #[20, 10, 5, 3]

#sorted : It will sorted in new copy 
li2 = [100,30,500,10]
sorted_li2 = sorted(li2)
print(sorted_li2) #[10, 30, 100, 500]
