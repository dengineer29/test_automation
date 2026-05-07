from abc import ABC, abstractmethod

class PrintJob(ABC):
    def __init__(self, user, filename, size, date):
        self.user = user
        self.filename = filename
        self.size = size
        self.date = date

    @abstractmethod
    def display_print(self):
        pass

    def print_status(self, status):
        self.status = status
        return f"User Name: {self.user}, File Name: {self.filename}, Status: {self.status}"
    
    @abstractmethod
    def cancel_job(self):
        return f"Cancel print job"

class ColorPrintJob(PrintJob):
    def __init__(self, user, filename, size, date, color):
        super().__init__(user, filename, size, date)
        self.color = color

    def display_print(self):
        return f"User Name: {self.user}, File Name: {self.filename}, Job Size: {self.size}, Date: {self.date}, Color: {self.color}"

    def cancel_job(self):
        return f"Cancel {self.color} print job" 

class BWPrintJob(PrintJob):
    def __init__(self, user, filename, size, date):
        super().__init__(user, filename, size, date)

    def display_print(self):
        return f"User Name: {self.user}, File Name: {self.filename}, Job Size: {self.size}, Date: {self.date} Black and White print"
    
    def cancel_job(self):
        return "Cancel BW print job"

#printjob1 = PrintJob("dani", "sample", "18kb", "04/05/2026")
colorprint = ColorPrintJob("skadi", "park.pdf", "100kb", "05/05/2026", "red")
bwprint = BWPrintJob("skadi", "arfarf.txt", "10kb", "07/05/2026")
    
jobs = [colorprint, bwprint]

for job in jobs:
    print(job.display_print())
    print(job.cancel_job()) 

