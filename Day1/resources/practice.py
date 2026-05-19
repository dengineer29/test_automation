#__init__ with a PrintQueue, create_color_job, create_bw_job, get_job_display, get_cancel_message, add_job_to_queue, get_queue_size, queue_is_empty.
import printjob

class PrintJobKeywords:

    def __init__(self):
        self._queue= printjob.PrintQueue()

    def create_print_job(self, job_data):
        if job_data["color_mode"] == "color":
            return printjob.ColorPrintJob(job_data["user"], job_data["filename"], job_data["size"], job_data["date"], job_data["printer"], job_data["color_mode"], job_data["color_type"], job_data["pages"])
        elif job_data["color_mode"] == "bw":
            return printjob.BWPrintJob(job_data["user"], job_data["filename"], job_data["size"], job_data["date"], job_data["printer"], job_data["color_mode"], job_data["pages"])

    def get_display(self, job):
        return job.display_print()
    
    def get_cancel_message(self, job):
        return job.cancel_job()
        
    def add_job_to_queue(self, job):
        self._queue.add(job)

    def get_queue_size(self):
        return len(self._queue._jobs)
    
    def get_status(self, job):
        return job.get_status()

    def queue_is_empty(self):
        if len(self._queue._jobs) == 0:
            return True
        else:
            return False
           
