import threading
import thread
import time

class MyThread(threading.Thread):
	def __init__(self,thread_id,name,counter):
		super(MyThread, self).__init__()
		self.thread_id = thread_id
		self.name = name
		self.counter = counter
	def run(self):
		print 'Starting '+ self.name
		print_time(self,self.counter,5)
		print 'Exiting'+ self.name
	def print_time(thread_name,delay,counter):
		while  counter:
			time.sleep(delay)
			print ' %s %s' % (thread_name,time.ctime(time.time()))
			counter -= 1
			
			pass