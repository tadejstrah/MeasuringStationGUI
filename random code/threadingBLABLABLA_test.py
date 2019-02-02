import queue
import threading

class SomeClass(threading.Thread):
    def __init__(self, q, loop_time = 1.0/60):
        self.q = q
        self.timeout = loop_time
        super(SomeClass, self).__init__()

    def onThread(self, function, *args, **kwargs):
        self.q.put((function, args, kwargs))

    def run(self):
        while True:
            try:
                function, args, kwargs = self.q.get(timeout=self.timeout)
                function(*args, **kwargs)
            except queue.Empty:
                self.idle()

    def idle(self):
        pass
        # put the code you would have put in the `run` loop here 

    def doSomething(self):
        pass

    def doSomethingElse(self):
        pass

