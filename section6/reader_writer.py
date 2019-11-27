import threading

read_wirte_lock = threading.Lock()
counter_lock = threading.Lock()
counter = 0


def read():
    counter_lock.acquire()
    if counter == 0:
        read_wirte_lock.acquire()
    counter += 1
    counter_lock.release()
    print("read")
    read_wirte_lock.acquire()
    counter -= 1
    if counter == 0:
        read_wirte_lock.release()
    counter_lock.release()
    

def write():
    read_wirte_lock.acquire()
    print("write")
    read_wirte_lock.release()
