import os
import sys

sys.path.append( os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) ) )

from rq import Worker, Queue, Connection
from app.utils.queue_manager import queue_manager

if __name__ == '__main__':
    with Connection( queue_manager.redis_conn ):
        worker = Worker( [ Queue( 'accounts_queue' ) ] )
        worker.work()
