import thread
import time


def print_time(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print '%s:%s' % (thread_name, time.ctime(time.time()))
try:
    thread.start_new_thread(print_time, ('Thread_1', 2))
    thread.start_new_thread(print_time, ('thread_2', 4))
except:
    print 'Error:unable to satart the thread'

while True:
    pass
