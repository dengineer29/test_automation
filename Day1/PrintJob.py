class PrintJob():
    def __init__(self, user, filename, size, date):
        self.user = user
        self.filename = filename
        self.size = size
        self.date = date

    def display_print(self):
        return f"User Name: {self.user}, File Name: {self.filename}, Job Size: {self.size}, Date: {self.date}"

    def print_status(self, status):
        self.status = status
        return f"User Name: {self.user}, File Name: {self.filename}, Status: {self.status}"
    
    def cancel_job(self):
        pass

printjob1 = PrintJob("dani", "sample", "18kb", "04/05/2026")

print(printjob1.display_print())