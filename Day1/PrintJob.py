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
        return f"Cancel print job"

class ColorPrintJob(PrintJob):
    def __init__(self, user, filename, size, date, color):
        super().__init__(user, filename, size, date)
        self.color = color

    def display_print(self):
        return f"User Name: {self.user}, File Name: {self.filename}, Job Size: {self.size}, Date: {self.date}, Color: {self.color}"

    
printjob1 = PrintJob("dani", "sample", "18kb", "04/05/2026")
colorprint = ColorPrintJob("skadi", "park.pdf", "100kb", "05/05/2026", "red")
colorprint.print_status("OK")

print(printjob1.display_print())
print(colorprint.display_print())
