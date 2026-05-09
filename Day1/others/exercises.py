# write PrintJob here
class PrintJob():
    def __init__(self, file, pages):
        self.file = file
        self.pages = pages
    
    def cancel(self):
        print("Canceling print job... done.")
    
class ColorPrintJob(PrintJob):
    def __init__(self, file, pages, color_profile):
        super().__init__(file, pages)
        self.color_profile = color_profile

    def cancel(self):
        super().cancel()
    
# write ColorPrintJob here


job = ColorPrintJob("photo.png", 2, "sRGB")
print(job.pages)         # 2
print(job.color_profile) # sRGB
job.cancel()             # Cancelling color job... done.