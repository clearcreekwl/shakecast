import time
from pydispatch import dispatcher

class Task(object):
    
    """
    Task objects are used to simplify running specific functions with
    specific conditions. A Task is basically just a function that
    remembers how it is supposed to run and can keep track of
    its own inputs and outputs
    """
    def __init__(self,
                 name="new_task",
                 task_id=None,
                 func=None,
                 conn=None,
                 args_in=None,
                 loop=False,
                 interval=100,
                 run_in = 0,
                 kill_time=None):
        self.name = name
        self.id = task_id
        self.func = func
        self.conn = conn
        self.args_in = args_in
        self.loop = loop
        self.interval = interval
        self.last_run = 0
        self.status = 'stopped'
        self.next_run = time.time() + run_in
        self.kill_time = None
        self.output = {'status': '',
                       'messege': ''}
        
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return "\n\n%s(id: %s, \n\
                   arguments: %s, \n\
                   loop: %s, \n\
                   interval: %s) status: %s" % (self.name,
                                                self.id,
                                                self.args_in,
                                                self.loop,
                                                self.interval,
                                                self.status)        
        
    def run(self):
        self.status = 'running'
        print 'Running: %s' % self.name
        if self.func is not None:
            try:
                if self.args_in is not None:
                    self.output = self.func(**self.args_in)
                    
                    self.status = 'finished'
                else:
                    self.output = self.func()
                    self.status = 'finished'
            except:
                self.status = 'failed'
                
            if self.loop is True:
                self.next_run = time.time() + self.interval
                self.last_run = time.time()