class Printer:
    def __init__(self, name, ip, model):
        self.name = name
        self.ip = ip
        self.model = model
    
    def set_status(self, status):
        self.status = status
        return self.status

    def print_job(self, doc_name, user, time):
        self.doc_name = doc_name
        self.user = user
        self.time = time
        return self.doc_name, self.user, self.time

    def __str__(self):
        return f"Printer: {self.name} | IP: {self.ip} | Model: {self.model}"

printer1 = Printer("lancia", "10.77.52.224", "MP 305+")
printer2 = Printer("mazda", "10.77.52.242", "MP 3055")
printer3 = Printer("volvo", "10.77.52.211", "MP 3055")

printer1.set_status("Not OK")
print(printer2.print_job("sample1", "dani", "8:31"))

print(printer1)
print(printer2)
print(printer3)