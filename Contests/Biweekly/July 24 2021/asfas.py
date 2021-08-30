from collections import queue

def fun():
    q = queue.Queue()
    for i in [3, 2, 1]:
        def f():
            time.sleep(i)
            q.put(i)
        threading.Thread(target=f).start()

print(fun(1000))