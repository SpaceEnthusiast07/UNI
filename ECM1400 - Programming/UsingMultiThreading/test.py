import threading, time, random

def printSomething(text):
	time.sleep(random.randint(0, 3))
	print(text)

x = threading.Thread(target=printSomething, args=("Print",))
y = threading.Thread(target=printSomething, args=("this",))
z = threading.Thread(target=printSomething, args=("now",))

x.start()
y.start()
z.start()