import threading
import time

x = 4096
lock = threading.Lock()
event = threading.Event()

# two example funtions
def HelloWorld():
    for i in range(100):
        print("Hello Worlds")

def NamePrint():
    for i in range(100):
        print("Wise One")
  
      
# Example funtions to show locking of threads       
def double():
    global x, lock
    lock.acquire()
    while x < 10000:
        x *= 2
        print(x)
        time.sleep(1)
    print("Reached Maximum!!")
    lock.release()

def half():
    global x, lock
    lock.acquire()
    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)
    print("Reached Minimum!!")
    lock.release()
    
def wait_event():
    print("Want to play a game. Waiting for your input...\n")
    event.wait()
    print("Hello buddy, let's start\n")
    

    
def main():
    # open two parallel threads from the main thread (print in parallel)
    t1 = threading.Thread(target=HelloWorld)
    t2 = threading.Thread(target=NamePrint)

    # print in parallel - might be delayed results
    t1.start()
    t2.start()

    # to allow the previous threads to finish and merge in main thread so the next step can execute
    t1.join()
    t2.join()
    print("Exiting")


    # Creating threads for locked threats
    t3 = threading.Thread(target=half)
    t4 = threading.Thread(target=double)

    # print in serial order.
    t3.start() # thread locked --> half funtion execute --> lock release
    t4.start() # thread locked --> double funtion execute --> lock release
    
    
    # Creating Event thread
    t5 = threading.Thread(target=wait_event)
    t5.start()
    
    # getting and calling the trigger
    x = input("Want to play the game --> (y/n)\n")
    if x == 'y':
        event.set()
    else:
        print("I am disappointed.")
    


if __name__ == '__main__':
    main()