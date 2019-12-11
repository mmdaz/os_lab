class Process:

    def __init__(self, cbt, start_time, priority):
        self.cbt = cbt
        self.start_time = start_time
        self.end_time = None
        self.priority = priority

    def run(self, ticks, quantum):
        if not self.is_finished(quantum=quantum):
            self.cbt -= ticks
        else:
            self.cbt = 0

    def is_finished(self, quantum):
        if self.cbt - quantum <= 0:
            return True
        else:
            return False

    def set_end_time(self, end_time):
        self.end_time = end_time
