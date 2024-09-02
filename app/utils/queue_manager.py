import redis
from rq import Queue
from rq.job import Job
from rq_scheduler import Scheduler
from datetime import datetime, timedelta

class QueueManager:
    def __init__(self):
        self.redis_conn = redis.Redis()
        self.queue = Queue( 'accounts_queue', connection = self.redis_conn )
        self.scheduler = Scheduler( queue = self.queue, connection = self.redis_conn )

    def enqueue_job( self, func, *args, **kwargs):
        return self.queue.enqueue( func, *args, **kwargs )
    
    def schedule_job( self, func, args = None, kwargs = None, interval = 300, repeat = None ):
        return self.scheduler.schedule(
            scheduled_time = datetime.utcnow(),
            func = func,
            args = args or (),
            kwargs = kwargs or {},
            interval = interval,
            repeat = repeat
        )

    def get_job( self, job_id ):
        return Job.fetch( job_id, connection = self.redis_conn )

queue_manager = QueueManager()
