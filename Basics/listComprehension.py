<<<<<<< HEAD
li1 = [1,2,3,4,5]
print(li1) #[1, 2, 3, 4, 5]
square_list = []
for i in li1:
    square_list.append(i**2)
print(square_list) #[1, 4, 9, 16, 25]

#Using list comprehension
li1 = [1,2,3,4,5]
duplicate_li1 = [i for i in li1]
#When we have if part then write it after for loop

even = [i for i in li1 if i%2 == 0]
sq_list = [i**2 for i in li1]
new_li1 = [ele+2 for ele in li1]
print(even) #[2, 4]
print(sq_list) #[1, 4, 9, 16, 25]
print(new_li1) #[3, 4, 5, 6, 7]

#When we have if-else both write it before for loop
even_odd = ['even' if i%2==0 else 'Odd' for i in li1]
print(even_odd) #['Odd', 'even', 'Odd', 'even', 'Odd']

#Multiple for loops inside list comprehension
li = [[10,20],[30,40],[50,60]]
new_list = [ele for i in li for ele in i]
print(new_list) #[10, 20, 30, 40, 50, 60]
=======
li1 = [1,2,3,4,5]
print(li1) #[1, 2, 3, 4, 5]
square_list = []
for i in li1:
    square_list.append(i**2)
print(square_list) #[1, 4, 9, 16, 25]

#Using list comprehension
li1 = [1,2,3,4,5]
duplicate_li1 = [i for i in li1]
#When we have if part then write it after for loop

even = [i for i in li1 if i%2 == 0]
sq_list = [i**2 for i in li1]
new_li1 = [ele+2 for ele in li1]
print(even) #[2, 4]
print(sq_list) #[1, 4, 9, 16, 25]
print(new_li1) #[3, 4, 5, 6, 7]

#When we have if-else both write it before for loop
even_odd = ['even' if i%2==0 else 'Odd' for i in li1]
print(even_odd) #['Odd', 'even', 'Odd', 'even', 'Odd']

#Multiple for loops inside list comprehension
li = [[10,20],[30,40],[50,60]]
new_list = [ele for i in li for ele in i]
print(new_list) #[10, 20, 30, 40, 50, 60]
>>>>>>> 6729aa240a7a25022ef447f4c282c6c15ddfe66b
