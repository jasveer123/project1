from threading import *
from time import sleep
class hello(Thread):
    def run(self):
        for i in range(50):
           print("hello")
           sleep(2)
     
class hi(Thread):
    def fun(self):
        for i in range(50):

          print("hi")
          sleep(2)



t1=hello()
t2=hi()
t1.start()
t2.start()

