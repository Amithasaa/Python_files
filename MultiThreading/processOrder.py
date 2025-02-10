import time
import threading
def process_request(user):
    print(f"Processing request for the {user}...")
    time.sleep(5)
    print(f"Request completed for {user}")
 
process_request("User 1")
process_request("User 2")
process_request("User 3")

t1 = threading.Thread(target = process_request, args= ("User 1"))
t2 = threading.Thread(target = process_request, args= ("User 2"))
t3 = threading.Thread(target = process_request, args= ("User 3"))

