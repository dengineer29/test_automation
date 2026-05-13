#__init__ with a PrintQueue, create_color_job, create_bw_job, get_job_display, get_cancel_message, add_job_to_queue, get_queue_size, queue_is_empty.
import printjob

class PrintJobKeywords:

    def __init__(self):
        self._queue= printjob.PrintQueue()

    def create_color_job(self, job):
        return printjob.ColorPrintJob(job)

    def get_job_display(self, job):
        return self._queue.print_jobList(job)
    
    def get_cancel_message(self, job):
        return self._queue.cancel(job)
        
    def add_job_to_queue(self, job):
        self._queue.add(job)

    def get_queue_size(self):
        return len(self._queue._jobs)


