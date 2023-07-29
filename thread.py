import threading
import time


class MonThread(threading.Thread):
    def __init__(self, until, name, event):
        threading.Thread.__init__(self)
        self.until = until
        self.name = name
        self.event = event

    def run(self):
        self.etat = True
        for i in range(0, self.until):
            print("Thread iteration ", self.name, " : ", i)
            time.sleep(0.08)
        self.event.set()


print("Starting...")

event = threading.Event()  # on crée un objet de type Event
event.clear()  # on désactive l'objet Event
m = MonThread(5, "A", event)  # créer un thread
m.start()  # démarre le thread
while not event.is_set():
    print("j'attend")
    event.wait(0.1)  # on attend jusqu'à ce que l'objet soit activé
# m1 = MonThread(3, "B", event)
# m1.start()

print("End")
