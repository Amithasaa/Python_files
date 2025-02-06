li = [10,20,30]                   
for idx,ele in enumerate(li):
    print(f"Index of {ele} is {idx}")
# output
#0 10
# 1 20
# 2 30

#Write a python program to print all even index element
li = [10,20,30,40]
for idx, ele  in enumerate(li,start=1):
    if idx % 2 == 0 :
        print(ele) #20 40
    