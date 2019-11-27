import threading

lock = threading.Lock()

counter = 0

def say_hello(n):
    global counter
    for i in range(0, 10):
        lock.acquire()
        counter += 1
        print(f'Thread {n}: {i} -> {counter}')
        lock.release()

if __name__ == "__main__":
    t1 = threading.Thread(target=say_hello, args=(10,))
    t2 = threading.Thread(target=say_hello, args=(10,))
    t1.start()
    t2.start()
