MULTISCHED
==========

### Description

Multisched is a lightweight function scheduler module for python


### Usage

```python
from multisched import Scheduler

def timestamp(s):
    print '%.2f : %s' % (time.time(), s)

s = Scheduler()
# -----------------------------------------.
#          loopdelay   initdelay   threads |
# -----------------------------------------`
@s.AddTask(  1.3,          0              )
def task1():
    timestamp('task1')

@s.AddTask(  1.0,          3              )
def task2():
    timestamp('task2')
    time.sleep(1.6)
    timestamp('task2 again')

@s.AddTask(  1.1,          0,         4   )
def task3():
    timestamp('task3')
    time.sleep(4.4)
    timestamp('task3 again')

print s
s.StartAllTasks()
try:
    raw_input()
except:
    pass
s.StopAllTasks()
```
