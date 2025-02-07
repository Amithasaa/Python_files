import time
import threading

print(threading.current_thread())
li1 = [1,2,3,4,5]
li2 = ['a','b','c','d','e']

def displayDigits(li1):
    print(t1.is_alive())
    print(threading.current_thread())
    for i in li1:
        print(i)
        time.sleep(2)
        
def displayLetters(li2):
    print(t1.is_alive())
    print(threading.current_thread())
    for i in li2:
        print(i)
        time.sleep(1)
        
t1 = threading.Thread(target=displayDigits, args=(li1,),name= "Tester") #(li1,) - tuple

t2 = threading.Thread(target=displayLetters, args=(li2,), name="Developer")
print(t1.is_alive())

t1.start()
t1.join()
t2.start()
