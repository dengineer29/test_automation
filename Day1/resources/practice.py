#__init__ with a PrintQueue, create_color_job, create_bw_job, get_job_display, get_cancel_message, add_job_to_queue, get_queue_size, queue_is_empty.
import printjob, printer_monitor
import subprocess, time
from log_parser import LogParser

class PrintJobKeywords:

    def __init__(self):
        self._queue= printjob.PrintQueue()
        self._parser = LogParser("/home/dengineer/Desktop/Study/test_automation/Day1/cups_sample.log")
        
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
    
    def submit_job_to_printer(self, filepath, printer="VirtualPrinter"):
        result = subprocess.run(
            ["lp", "-d", printer, filepath],
            capture_output=True, text=True
        )
        time.sleep(2) # give CUPS time to process
        return result.stdout.strip()

    # Add these methods inside PrintJobKeywords
    def load_log(self, filepath):
        self._parser = LogParser(filepath)

    def get_total_jobs(self):
        return self._parser.total_jobs()

    def get_total_pages(self):
        return self._parser.total_pages()

    def get_jobs_for_printer(self, printer):
        return len(self._parser.jobs_for_printer(printer))

    def get_top_user(self):
        return self._parser.top_user()
    
class PrinterMonitor:
    def __init__(self):
        self._monitor = printer_monitor.PrinterMonitor("localhost", "public", "v2c")

    def get_printer_status(self):
        #return self._monitor.is_ready()
        return 3

    def has_toner(self):
        #return self._monitor.has_toner()
        return 21

    def get_page_count(self):
        return self._monitor.get_page_count()

