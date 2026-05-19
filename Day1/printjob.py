from abc import ABC, abstractmethod

class PrintJob(ABC):
    def __init__(self, user, filename, size, date, printer, color_mode, color_type, pages):
        self.user = user
        self.filename = filename
        self.size = size
        self.date = date
        self.printer = printer
        self.pages = pages
        self.color_mode = color_mode
        self.color_type = color_type

    @abstractmethod
    def display_print(self):
        pass
    
    @abstractmethod
    def cancel_job(self):
        pass

class ColorPrintJob(PrintJob):
    def __init__(self,user, filename, size, date, printer, color_mode, color_type, pages):
        super().__init__(user, filename, size, date, printer, color_mode, color_type, pages)
        self.color_type = color_type
        self.color_mode = color_mode

    def display_print(self):
        return f"User Name: {self.user}, File Name: {self.filename}, Job Size: {self.size}, Date: {self.date}, Printer: {self.printer}, Color: {self.color_type}, Pages: {self.pages}"

    def cancel_job(self):
        return f"Cancel {self.color_type} print job" 

class BWPrintJob(PrintJob):
    def __init__(self, user, filename, size, date, printer, color_mode, color_type, pages):
        super().__init__(user, filename, size, date, printer, color_mode, color_type, pages)

    def display_print(self):
        return f"User Name: {self.user}, File Name: {self.filename}, Job Size: {self.size}, Date: {self.date}, Printer: {self.printer}, Pages: {self.pages}, Color Mode: {self.color_mode}"
    
    def cancel_job(self):
        return "Cancel BW print job"

class PrintQueue():
    def __init__(self):
        self._jobs = []

    def add(self, job):
        self._jobs.append(job)

    def cancel(self, job):
        self._jobs.remove(job)

    def print_jobList(self):
        for job in self._jobs:
            print(job.display_print())
