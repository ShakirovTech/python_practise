class ErrorLogIterator:
    def __init__(self, logs):
        self.logs = logs
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.logs):
            cur = self.logs[self.index]
            self.index += 1
            if 'ERROR:' in cur:
                return cur
        raise StopIteration


logs = [
    "INFO: Server launched",
    "DEBUG: Connecting to database",
    "ERROR: Time-out connection",
    "INFO: Request processed",
    "ERROR: Denial of access",
    "WARNING: High load"
]

error_iterator = ErrorLogIterator(logs)

# iteration invokes __iter__ under the hood and calls __next__ until StopIteration is raised
for log in error_iterator:
    print(log)
