MULTISCHED
==========

### Description

Multisched is a lightweight function scheduler module for python


### Usage

```python
from multisched import Scheduler
import time

s = Scheduler()

def timestamp(s):
    print '%.2f : %s' % (time.time(), s)

class Action():
    def __init__(self, name):
        self.__name__       = name
        self.call_counter   = 0

    def __call__(self):
        self.call_counter  += 1
        print 'I am %s (%d)' % (self.__name__, self.call_counter)

# ----------------------------------.
#                                   |
#  TASK PARAMS:                     |
#                                   |
#    loopdelay:   float, required   |
#    initdelay:   float, default=0  |
#    threads  :   int  , default=0  |
#                                   |
# ----------------------------------`
@s.AddTask(loopdelay=1.3)
def task1():
    timestamp('task1')

@s.AddTask(loopdelay=1.0, initdelay=3)
def task2():
    timestamp('task2')
    time.sleep(1.6)
    timestamp('task2 again')

@s.AddTask(loopdelay=1.1, threads=4)
def task3():
    timestamp('task3')
    time.sleep(4.4)
    timestamp('task3 again')

s.AddTasks({'action'    : Action('Agent%03d' % n)
           ,'loopdelay' : 0.6
           ,'initdelay' : 1.1
           ,'threads'   : 0
           } for n in xrange(42))
print s
s.StartAllTasks()
try:
    raw_input()
except:
    pass
s.StopAllTasks()

```
