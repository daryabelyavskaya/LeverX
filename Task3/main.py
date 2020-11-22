from threading import Thread, Lock

a = 0
lock = Lock()


def function(arg):
    global a
    lock.acquire()
    for _ in range(arg):
        # we can call lock.acquire() and lock.release() inside the loop, but calling this functions
        # is much more consuming than incrementing a variable, so in this specific situation much suitable to cover
        # in mutex whole loop.
        # lock.acquire()
        a += 1
        # lock.release()
    lock.release()


def main():
    threads = []
    for i in range(5):
        thread = Thread(target=function, args=(1000000,))
        thread.start()
        threads.append(thread)
    [t.join() for t in threads]
    print("----------------------", a)


main()
