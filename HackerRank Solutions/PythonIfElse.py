n = int(input())
if n%2 != 0:
    print("Weird")
elif n%2 == 0 and 2<=n<=5:
    print("Not weird")
elif n%2==0 and 6<=n<=20:
    print("Weird")
elif n > 20:
    print("Not Weird")
    