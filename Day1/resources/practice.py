#__init__ with a PrintQueue, create_color_job, create_bw_job, get_job_display, get_cancel_message, add_job_to_queue, get_queue_size, queue_is_empty.
import printjob

class PrintJobKeywords:

    def __init__(self):
        self._queue= printjob.PrintQueue()

    def create_color_job(self, user, filename, size, date, printer, color):
        return printjob.ColorPrintJob(user, filename, size, date, printer, color)

    def create_bw_job(self, user, filename, size, date, printer):
        return printjob.BWPrintJob(user, filename, size, date, printer)

    def get_display(self, job):
        return job.display_print()
    
    def get_cancel_message(self, job):
        return job.cancel_job()
        
    def add_job_to_queue(self, job):
        self._queue.add(job)

    def get_queue_size(self):
        return len(self._queue._jobs)
    
    def queue_is_empty(self):
        if len(self._queue._jobs) == 0:
            return True
        else:
            return False