class LogEntry:
    def __init__(self, printer, user, job_id, pages):
        self.printer = printer
        self.user = user
        self.job_id = job_id
        self.pages = int(pages)

    @classmethod
    def from_line(cls, line):
        parts = line.split()
        # parts: [0]printer [1]user [2]job_id [3]date [4]pages [5]copies [6]billing [7]host
        return cls(parts[0], parts[1], parts[2], parts[4])

class LogParser:
    def __init__(self, filepath):
        self._entries = []
        with open(filepath) as f:
            for line in f:
                if line.strip():
                    self._entries.append(LogEntry.from_line(line.strip()))

    def total_jobs(self): return len(self._entries)
    def total_pages(self): return sum(e.pages for e in self._entries)
    def jobs_for_printer(self, p): return [e for e in self._entries if e.printer==p]
    def top_user(self):
        counts={}
        for e in self._entries: counts[e.user]=counts.get(e.user,0)+1
        return max(counts, key=counts.get)