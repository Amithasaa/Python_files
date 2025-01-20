<<<<<<< HEAD
#list_name[start:end:steps]
'''
List slicing is usedto create sublist from main list
It won't modify the original list

reverse list: [::-1]
last ele: [-1::]
'''


li1 = [10,20,30,40,50,60]
sub_list1 = li1[0:4:1]
print(sub_list1) #[10, 20, 30, 40]

sub_list2 = li1[1::]
print(sub_list2) #[20, 30, 40, 50, 60]

sub_list3 = li1[::2]
print(sub_list3) #[10, 30, 50]

sub_list4_rev = li1[::-1]
print(sub_list4_rev) #[60, 50, 40, 30, 20, 10]

sub_list5 = li1[-1::]
=======
#list_name[start:end:steps]
'''
List slicing is usedto create sublist from main list
It won't modify the original list

reverse list: [::-1]
last ele: [-1::]
'''


li1 = [10,20,30,40,50,60]
sub_list1 = li1[0:4:1]
print(sub_list1) #[10, 20, 30, 40]

sub_list2 = li1[1::]
print(sub_list2) #[20, 30, 40, 50, 60]

sub_list3 = li1[::2]
print(sub_list3) #[10, 30, 50]

sub_list4_rev = li1[::-1]
print(sub_list4_rev) #[60, 50, 40, 30, 20, 10]

sub_list5 = li1[-1::]
>>>>>>> 6729aa240a7a25022ef447f4c282c6c15ddfe66b
print(sub_list5) #[60]