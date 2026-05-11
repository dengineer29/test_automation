from printjob import ColorPrintJob, BWPrintJob

class PrintJobKeywords:

    def create_color_job(self, user, filename, size, date, printer, color):
        return ColorPrintJob(user, filename, size, date, printer, color)

    def create_bw_job(self, user, filename, size, date, printer):
        return BWPrintJob(user, filename, size, date, printer)

    def get_display(self, job):
        return job.display_print()

    def get_cancel_message(self, job):
        return job.cancel_job()