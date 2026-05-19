from abc import ABC, abstractmethod


class PrintJob(ABC):
    def __init__(self, user, filename, size, date, printer, color_mode, color_type, pages):
        self.user = user
        self.filename = filename
        self.size = size
        self.date = date
        self.printer = printer
        self.color_mode = color_mode
        self.color_type = color_type
        self.pages = pages
        self._status = "pending"          # initialised here so it always exists from the moment a job is created

    @abstractmethod
    def display_print(self):
        pass

    @abstractmethod
    def cancel_job(self):
        pass

    def get_status(self):
        # returns the current status string — Robot tests can assert: Should Be Equal  ${status}  pending
        return self._status

    def process(self):
        # marks the job as processed and returns a summary — called by PrintQueue.process_next()
        self._status = "processed"
        return f"Processing: {self.display_print()}"

    def is_pending(self):
        # returns True if job hasn't been processed or cancelled yet — used with Should Be True in Robot
        return self._status == "pending"

    def is_processed(self):
        # returns True if job was successfully processed — useful for post-process assertions
        return self._status == "processed"

    def is_cancelled(self):
        # returns True if job was cancelled — useful for asserting cancel worked correctly
        return self._status == "cancelled"


class ColorPrintJob(PrintJob):
    def __init__(self, user, filename, size, date, printer, color_mode, color_type, pages):
        super().__init__(user, filename, size, date, printer, color_mode, color_type, pages)
        # color_mode and color_type are already set by super().__init__()
        # removed the duplicate self.color_type and self.color_mode assignments from your original

    def display_print(self):
        return (
            f"User Name: {self.user}, File Name: {self.filename}, "
            f"Job Size: {self.size}, Date: {self.date}, Printer: {self.printer}, "
            f"Color Mode: {self.color_mode}, Color: {self.color_type}, Pages: {self.pages}"
        )

    def cancel_job(self):
        self._status = "cancelled"        # update status so is_cancelled() returns True after this call
        return f"Cancel {self.color_type} print job"

    def get_color_type(self):
        # exposes color_type as a standalone keyword — Robot can capture and assert on it directly
        return self.color_type

    def get_color_mode(self):
        # exposes color_mode as a standalone keyword — e.g. assert color_mode equals "color"
        return self.color_mode

    def get_pages(self):
        # exposes pages as a standalone keyword — Robot: Should Be Equal As Integers  ${pages}  5
        return self.pages


class BWPrintJob(PrintJob):
    def __init__(self, user, filename, size, date, printer, color_mode, pages):
        super().__init__(user, filename, size, date, printer, color_mode, pages)

    def display_print(self):
        return (
            f"User Name: {self.user}, File Name: {self.filename}, "
            f"Job Size: {self.size}, Date: {self.date}, Printer: {self.printer}, "
            f"Pages: {self.pages}, Color Mode: {self.color_mode}"
        )

    def cancel_job(self):
        self._status = "cancelled"        # update status so is_cancelled() returns True after this call
        return "Cancel BW print job"

    def get_pages(self):
        # exposes pages as a standalone keyword — same as ColorPrintJob for consistent Robot keyword use
        return self.pages


class PrintQueue:
    def __init__(self):
        self._jobs = []                   # private list — only modified through the methods below

    def add(self, job):
        # adds a job to the end of the queue
        self._jobs.append(job)

    def cancel(self, index):
        # takes an index number so CLI and Robot tests can reference jobs by their position
        if 0 <= index < len(self._jobs):
            job = self._jobs[index]
            message = job.cancel_job()    # call cancel_job() on the job to update its status and get the message
            self._jobs.pop(index)         # remove the job from the queue after cancelling
            return message
        return "Invalid index. No job cancelled."

    def process_next(self):
        # processes and removes the first job in the queue (FIFO — first in, first out)
        if self._jobs:
            job = self._jobs.pop(0)       # pop from front of list to maintain queue order
            return job.process()          # call process() which updates status and returns a summary string
        return "Queue is empty. No jobs to process."

    def get_queue_size(self):
        # returns number of jobs in queue — Robot: ${size}=  Get Queue Size  then  Should Be Equal As Integers
        return len(self._jobs)

    def is_empty(self):
        # returns True when queue has no jobs — Robot: Should Be True  ${empty}
        return len(self._jobs) == 0

    def get_job_at(self, index):
        # returns a specific job object by index — lets Robot inspect individual jobs in the queue
        if 0 <= index < len(self._jobs):
            return self._jobs[index]
        return None                       # returns None if index is out of range — Robot test can assert this

    def print_jobList(self):
        # prints every job with its index number and current status so the user can reference by number
        if not self._jobs:
            print("Queue is empty.")
            return
        for i, job in enumerate(self._jobs):    # enumerate() gives both the index and the job in one loop
            print(f"[{i}] {job.display_print()} | Status: {job.get_status()}")
